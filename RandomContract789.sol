// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RandomContract789 {
    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    function withdraw() external {
        require(msg.sender == owner, "Only the owner can withdraw");
        owner.transfer(address(this).balance);
    }

    // A payable function to receive Ether
    function fundContract() public payable {
        // This function can receive Ether
    }

    // Function to check the balance of the contract
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}