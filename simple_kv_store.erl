-module(simple_kv_store).
-behaviour(gen_server).

%% API
-export([start_link/0, put/2, get/1, stop/1]).

%% gen_server callbacks
-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3]).

-record(state, {data = #{}}).

%%%===================================================================
%%% API
%%%===================================================================

start_link() ->
    gen_server:start_link(?MODULE, [], []).

put(Pid, Key, Value) ->
    gen_server:call(Pid, {put, Key, Value}).

get(Pid, Key) ->
    gen_server:call(Pid, {get, Key}).

stop(Pid) ->
    gen_server:stop(Pid).

%%%===================================================================
%%% gen_server callbacks
%%%===================================================================

init([]) ->
    {ok, #state{}}.

handle_call({put, Key, Value}, _From, State) ->
    NewData = State#state.data#{Key => Value},
    {reply, ok, State#state{data = NewData}};

handle_call({get, Key}, _From, State) ->
    Value = maps:get(Key, State#state.data, undefined),
    {reply, Value, State};

handle_call(_Request, _From, State) ->
    {reply, {error, unknown_call}, State}.

handle_cast(_Msg, State) ->
    {noreply, State}.

handle_info(_Info, State) ->
    {noreply, State}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.