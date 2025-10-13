-module(random_server_443585).
-behaviour(gen_server).
%% API
-export([start_link/1, get_state/1, update_state/2]).

%% gen_server callbacks
-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3]).

-record(state, {value}).

start_link(InitialValue) ->
    gen_server:start_link(?MODULE, InitialValue, []).

get_state(Pid) ->
    gen_server:call(Pid, get_value).

update_state(Pid, NewValue) ->
    gen_server:cast(Pid, {set_value, NewValue}).

init(InitialValue) ->
    {ok, #state{value = InitialValue}}.

handle_call(get_value, _From, State) ->
    {reply, State#state.value, State}.

handle_cast({set_value, NewValue}, State) ->
    {noreply, State#state{value = NewValue}}.

handle_info(_Info, State) ->
    {noreply, State}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.
