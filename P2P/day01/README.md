# PoC P2P Pool 2025 - Day 01 - Solidity

✔️ You'll learn how to create a smart contract and how to use variables and visibilities.

✔️ You'll learn how to create and use functions and modifiers.

✔️ You'll learn what wei, gwei and ether are and how to use it.

✔️ You'll learn how to create and use hashes, events & errors.

✔️ You'll learn how to test your smart contracts with foundry.

## Introduction

Solidity is a programming language for writing smart contracts.
It is used for implementing smart contracts on various blockchain platforms, most notably, [Ethereum](https://ethereum.org/fr/).

A smart contract is a program that is stored and executed on a blockchain.
It's written in Solidity and compiled to [bytecode](https://docs.soliditylang.org/en/latest/metadata.html).
This bytecode is then deployed on the blockchain and it's possible to interact with it by sending transactions.

## Step 0 - Setup

Please refer to the [SETUP.md](./SETUP.md) file.

## Step 1 - Smart Contract

### :bookmark_tabs: **Description**:

In this first step, you will learn how to create a smart contract.
A Solidity smart contract is formed like this :

```solidity
// SPDX-License-Identifier: MIT       // License associated with the contract
pragma solidity ^0.8.20;              // Solidity compiler version

contract SmartContract {              // Smart contract declaration
    // ...
}
```

> 💡 The `^` symbol denotes the pragma directive, specifying the compiler version or range for compatibility, in this example the contract is compatible in versions 0.8.0 and later but not 0.9.0.

### :pushpin: **Tasks**:

- Remove the `Counter.sol` file from the `src` folder.

- Remove the `Counter.s.sol` file from the `script` folder.

- Create a new file `SmartContract.sol` in the `src` folder.

- In this file, create a new smart contract.

### :books: **Documentation**:

- [Smart Contract Introduction](https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html)
- [Smart Contract example](https://solidity-by-example.org/hello-world/)

## Step 2 - Variables types

### :bookmark_tabs: **Description**:

With Solidity, you have access to different types of variables :

- Signed integers
- Unsigned integers
- Strings
- Booleans
- Addresses
- And many more...

You will have to create variables.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a variable `halfAnswerOfLife` with value `21`

- Create a variable `_youAreACheater` with value `-42`

- Create a variable `PoCIsWhat` with value `PoC is good, PoC is life.`

- Create a variable `_areYouABadPerson` with value `false`

- Create a variable `myEthereumContractAddress` with value the current contract address

- Create a variable `myEthereumAddress` with value the current user address

### :books: **Documentation**:

- [Variables types](https://docs.soliditylang.org/en/latest/types.html#value-types)
- [Variables example](https://solidity-by-example.org/variables/)
- [Members of addresses](https://docs.soliditylang.org/en/latest/types.html#members-of-addresses)

## Step 3 - Visibility

### :bookmark_tabs: **Description**:

In Solidity, you can define the visibility of your variables and functions.

There are 4 types of visibility :

- `public` : The variable or function is accessible from everywhere
  > 💡 The compiler automatically generates getter functions for public variables
- `private` : The variable or function is accessible only from the current contract
- `internal` : The variable or function is accessible only from the current contract and from contracts that inherit it
- `external` : The function is only accessible outside the contract, variables can't be `external`
  > 💡 By default, variables are `internal`

You will have to modify the visibility of your variables created in the previous step.
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Modify the visibility to `public` for:

  - `halfAnswerOfLife`
  - `myEthereumContractAddress`
  - `myEthereumAddress`
  - `PoCIsWhat`

- Modify the visibility to `internal` for:

  - `_areYouABadPerson`

- Modify the visibility to `private` for:

  - `_youAreACheater`

A good practice is to start the name of private and internal variables or functions with a `_`. It allows you to quickly know the visibility of a variable or function.

### :books: **Documentation**:

- [Visibility documentation](https://docs.soliditylang.org/en/latest/contracts.html#visibility-and-getters)
- [Visibility example](https://solidity-by-example.org/visibility/)
- [Getter functions](https://docs.soliditylang.org/en/latest/contracts.html#getter-functions)

## Step 4 - Variables types #2

### :bookmark_tabs: **Description**:

There are other types of variables that you can use in Solidity:

- `bytes` : Store a sequence of bytes
- `mapping` : Store data in a key-value format
- `array` : Store data in a list format
- `struct` : Store data in a structure format
- `enum` : Store data in a list format with a name for each value

You will have to create variables.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a variable `whoIsTheBest` with value `0x4c75636173206327657374206c65206265737400000000000000000000000000`

- Create a variable `myGrades`

  - This variable is a mapping with key `string` and value `uint256`

- Create a variable `myPhoneNumber` with value `06`, `65`, `70`, `67`, `61`

  - This variable is an array of `string`
  - This variable has a length of `5`

- Create an enum `roleEnum` with values `STUDENT`, `TEACHER`

- Create a structure `informations` with values `firstName`, `lastName`, `age`, `city`, `role`

  - `firstname` is a `string`
  - `lastName` is a `string`
  - `age` is a `uint8`
  - `city` is a `string`
  - `role` is a `roleEnum`

- Create a variable `myInformations` with your personal informations

### :books: **Documentation**:

- [Variables types documentation](https://docs.soliditylang.org/en/latest/types.html#value-types)
- [Bytes documentation](https://docs.soliditylang.org/en/latest/types.html#fixed-size-byte-arrays)
- [Mapping Types documentation](https://docs.soliditylang.org/en/latest/types.html#mapping-types)
- [Arrays documentation](https://docs.soliditylang.org/en/latest/types.html#arrays)
- [Enums documentation](https://docs.soliditylang.org/en/latest/types.html#enums)
- [Structs documentation](https://docs.soliditylang.org/en/latest/types.html#structs)
- [Examples](https://solidity-by-example.org/)

## Step 5 - Functions

### :bookmark_tabs: **Description**:

Create variables is cool, but you can also create functions.

A function is a block of code that is executed when it is called.\
You can pass data to a function, and the function will return data as a result.\
A function can also modify your contract (its variables/balance) or the balance of the user that interacts with it.

There are 4 types of functions :

- `view` : The function is read-only
- `pure` : The function is read-only and does not even read the state or the environment
- `payable` : The function can receive ethers
- No type: The function can modify the state

You will have to create functions.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a function `getHalfAnswerOfLife` that returns `halfAnswerOfLife`

  - This function is `public`

- Create a function `_getMyEthereumContractAddress` that returns `myEthereumContractAddress`

  - This function is `internal`

- Create a function `getPoCIsWhat` that returns `PoCIsWhat`, use `string memory` as return type, we will see why later

  - This function is `external`

- Create a function `_setAreYouABadPerson` that returns nothing
  - This function is `internal`
  - This function takes a `bool` as parameter
  - This function modifies `_areYouABadPerson` with the parameter

Another good practice is to put a `_` at the beginning of the parameter name.

> :warning: Don't forget to define the type of your functions

### :books: **Documentation**:

- [Functions documentation](https://docs.soliditylang.org/en/latest/contracts.html#functions)
- [Functions type](https://docs.soliditylang.org/en/latest/contracts.html#state-mutability)
- [Functions example](https://solidity-by-example.org/function/)

## Step 6 - Testing with Foundry

### :bookmark_tabs: **Description**:

Now that you have created your smart contract, you will have to test it. For this, you will use [Foundry](https://book.getfoundry.sh/forge/writing-tests). Foundry is a tool that allows you to test your smart contract. It is very useful to test your smart contract before deploying it on the blockchain because once it is deployed, it is impossible to modify it.

### :pushpin: **Tasks**:

- Remove the `Counter.t.sol` file from the `test` folder.
- Create a new file `SmartContract.t.sol` in the `test` folder.
  - This file will contain the tests of your smart contract
- Create a contract helper `SmartContractHelper`.
  - This contract must inherit from your smart contract to access its variables and functions.
  - Add some functions who return the internal variables or call internal functions that you will test
- Create a contract `SmartContractTest` who inherit from `Test` contract.
  - You have to import `Test` contract, this one is contained in lib/forge-std folder.
  - add a `smartContract` variable of type `SmartContractHelper`
- Create a `setUp` function which will be executed before each test.
  - initialize the `smartContract` variable with a new `SmartContractHelper`
- Create the next public functions to test your smart contract, by checking the function returned value, with the `smartContract` variable:
  - `testGetHalfAnswerOfLife` : This function will test the function `getHalfAnswerOfLife`
  - `testSetAreYouABadPerson` : This function will test the function `_setAreYouABadPerson`
  - `testMyInformations` : This function will test the variable `myInformations`
- Execute the command [`forge test`](https://book.getfoundry.sh/reference/forge/forge-test) to run the tests.
  - You can use `forge test -vvvv` to show more information.

> 💡 You need to create a contract helper to test internal variables or functions.
> 💡 You can use the function `assertEq()` to test the returned value of a function with the correct value.

Correct your smart contract, if you have errors.

#### Bonus tasks:
  - `testGetMyEthereumContractAddress` : This function will test the function `_getMyEthereumContractAddress`
  - `testMyEthereumAddress` : This function will test the variable `myEthereumAddress`


### :books: **Documentation**:

- [Foundry testing documentation](https://book.getfoundry.sh/forge/writing-tests)
- [Forge test documentation](https://book.getfoundry.sh/reference/forge/forge-test)
- [Test internal function](https://book.getfoundry.sh/tutorials/best-practices#test-harnesses)

## Step 7 - Data Location

### :bookmark_tabs: **Description**:

In Solidity, you can define the location of your variables. There are 3 types of location:

- `storage` : The variable is stored on the blockchain, by default, variables in the contract are `storage`
- `memory` : The variable is stored in memory
- `calldata` : The variable is stored in memory and it is read-only

Choose the correct data location is very important because it can have an impact on the cost of the transaction. For example, if you use `memory` for a variable that you don't need to edit use instead `calldata`, it will cost less gas.

You will have to create functions to correctly understand data location. For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a function `editMyCity` that returns nothing
  - This function is `public`
  - This function takes a `string` as parameter
  - This function modifies your city in `myInformations` with the parameter

- Create a function `getMyFullName` that returns my full name
  - This function is `public`
  - This function returns a `string`
  - This function returns the concatenation of `firstName` and `lastName` from `myInformations` with a space between them

> :warning: Choose the correct data location for parameters and return values

Create 2 tests functions for these functions.

### :books: **Documentation**:

- [Data location documentation](https://docs.soliditylang.org/en/latest/types.html#data-location)
- [Data location example](https://solidity-by-example.org/data-locations/)

## Step 8 - Modifier

### :bookmark_tabs: **Description**:

A modifier is a function that is executed before a function.\
For example, you can use a modifier to check if the user is allowed to execute a function.

You will have to create a modifier.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a function `completeHalfAnswerOfLife` that returns nothing

  - This function is `public`
  - This function modifies `halfAnswerOfLife` by adding `21`

- Create a modifier `onlyOwner`

  - This modifier checks if the caller of the function is the owner of the contract

- Add the modifier `onlyOwner` to the function `completeHalfAnswerOfLife`  


Create 2 tests functions for this function :
- one call the function with the contract owner address which will pass
- one call the function with another address which will fail
> 💡 Take a look at the vm.startPrank() and vm.expectRevert() to change the function caller address

### :books: **Documentation**:

- [Modifiers documentation](https://docs.soliditylang.org/en/latest/contracts.html#function-modifiers)
- [Modifiers example](https://solidity-by-example.org/function-modifier/)
- [Start prank](https://book.getfoundry.sh/cheatcodes/start-prank)
- [Expect revert](https://book.getfoundry.sh/cheatcodes/expect-revert)

## Step 9 - Hashes

### :bookmark_tabs: **Description**:

Hashes are used to encrypt data in order to make it unreadable.\
Hashes are very useful to secure data.

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a function `hashMyMessage` that returns a `bytes32`
  - This function is `public`
  - This function takes a `string` as parameter
  - This function hashes the parameter with `keccak256` and returns the result

Create a test function to test this function.

### :books: **Documentation**:

- [Keccak256 documentation](https://docs.soliditylang.org/en/latest/units-and-global-variables.html#mathematical-and-cryptographic-functions)
- [Keccak256 example](https://solidity-by-example.org/hashing/)

## Step 10 - Gas, wei, gwei and ether

### :bookmark_tabs: **Description**:

Gas is the unit used to measure the cost of a transaction. It is used to pay, in ETH, the miners for the execution of the transaction. The more there is gas, the more the transaction will be executed quickly. The gas was introduced to prevent spamming the network. The more the network is used, the more the gas will be expensive.

Wei, gwei and ether are the unit used to measure the value of a transaction. There are used to pay the transaction fees. A transaction can be anything: money transfer, smart contract interaction, etc...

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Add a variable `balances`

  - This variable is `public`
  - This variable is a mapping with key `address` and value `uint256`
  - This mapping will store the balances of each address

- Create a function `getMyBalance` that returns a `uint256`

  - This function is `public`
  - This function returns the balance of the user who calls the function

- Create a function `addToBalance`

  - This function is `public`
  - This function takes no parameter
  - This function adds the value send with the transaction to the balance of the user who calls the function

- Create a function `withdrawFromBalance`
  - This function is `public`
  - This function takes a `uint256` as parameter
  - This function withdraws the value of the parameter from the balance of the user who calls the function

> :warning: Don't forget to define the type of your functions to accept ethers

> :warning: Don't forget to verifie that the transfer was successful

Create 2 tests to test the `addToBalance` and `withdrawFromBalance` functions.

### :books: **Documentation**:

- [Ether units documentation](https://docs.soliditylang.org/en/latest/units-and-global-variables.html#ether-units)
- [Ether units example](https://solidity-by-example.org/ether-units/)
- [Receive ether function documentation](https://docs.soliditylang.org/en/latest/contracts.html#receive-ether-function)
- [Sending ether example](https://solidity-by-example.org/sending-ether/)

## Step 11 - Events

### :bookmark_tabs: **Description**:

Events are used to log data.\
They are useful to know what happened in the smart contract.

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create an event `BalanceUpdated`

  - This event takes a `address indexed` as parameter
  - This event takes a `uint256` as parameter

- Add the event `BalanceUpdated` to the function `addToBalance` and `withdrawFromBalance`

> The `indexed` keyword is used to allow filtering of the event. It is useful to filter events by address. You can add up to 3 `indexed` parameters. You can't filter events by `string` or `bytes`

Edit your 2 previous tests to test if the event was correctly emitted.

### :books: **Documentation**:

- [Events documentation](https://docs.soliditylang.org/en/latest/contracts.html#events)
- [Events example](https://solidity-by-example.org/events/)
- [Expect emit documentation](https://book.getfoundry.sh/cheatcodes/expect-emit)

## Step 12 - Errors

### :bookmark_tabs: **Description**:

Errors are used to return an error message.\
They are useful to know why a transaction failed.

There is two ways to throw an error :

- With the usage of `require`, `assert` or `revert`
- With the usage of `error`

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create an error `InsufficientBalance`

  - This error takes a `uint256` as parameter of the quantity of ethers available in the balance of the user
  - This error takes a `uint256` as parameter of the quantity of ethers requested by the user

- Add the error `InsufficientBalance` to the function `withdrawFromBalance`
  - This error is thrown if the balance of the user is inferior to the value requested

Create a test to test if the function `withdrawFromBalance` throws the error `InsufficientBalance` if the balance of the user is inferior to the value requested.

### :books: **Documentation**:

- [Error handling documentation](https://docs.soliditylang.org/en/latest/control-structures.html#error-handling-assert-require-revert-and-exceptions)
- [Errors revert documentation](https://docs.soliditylang.org/en/latest/contracts.html#errors-and-the-revert-statement)
- [Errors example](https://solidity-by-example.org/error/)

## Step 13 - Inheritance

### :bookmark_tabs: **Description**:

Inheritance is used to reuse code.\
It is useful to avoid code duplication. It is also useful to create a contract that inherits from another contract. This contract will have access to the variables and functions (not the private ones) of the contract that it inherits.

There are certain types of contracts that must be inherited to be deployed. We call them `interface` and `abstract` contracts.

- `interface` : This contract is used to define the functions (their prototype), the events, the errors and the structures that must be implemented in the contract that inherits it. It can define only functions that are not `private` or `internal`.
  > The function prototype must be defined as `external` and can't have a body.
- `abstract` : This contract is used to define the functions, the events, the errors, the structures and also the variables that must be implemented in the contract that inherits it.
  > The function can have any visibility and can have a body.

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a folder `interfaces` in the `src` folder.
- Create an `interface` contract `ISmartContract` in the `interfaces` folder.
  - This contract must define events, errors, structures, enums and functions of `SmartContract`
  - `SmartContract` must inherit from `ISmartContract`
  - You can remove the events, errors, structures and enums of `SmartContract` because they are already defined in `ISmartContract`

### :books: **Documentation**:

- [Inheritance documentation](https://docs.soliditylang.org/en/latest/contracts.html#inheritance)
- [Interface documentation](https://docs.soliditylang.org/en/latest/contracts.html#interfaces)
- [Abstract documentation](https://docs.soliditylang.org/en/latest/contracts.html#abstract-contracts)
- [Inheritance example](https://solidity-by-example.org/inheritance/)
- [Interface example](https://solidity-by-example.org/interface/)

## Step 14 (BONUS) - Storage & Assembly

### :bookmark_tabs: **Description**:

Now that you have the basics you will deep dive into Solidity. In this task you will learn about the storage layout. You will learn how to use the assembly block to access to the storage directly and to store data in the blockchain.

In Solidity, you can use assembly block to write assembly code. Assembly code is a low-level programming language. It is used to write code that is executed directly by the EVM (Ethereum Virtual Machine). It is useful to optimize your smart contract.

### :pushpin: **Tasks**:

- Create a new solidity contract, with theses variables:

  ```solidity
  address mat;

  uint eo;

  bool m;

  address a;

  uint[] mmm;

  mapping(string => mapping (uint => uint)) chall;

  string[5] mateo;
  ```

- Your contract must have 2 functions:

    ```solidity
    function get(uint256 slot, uint256 offset) public view returns (bytes32 value)
    ```
    - This function must return the value of the storage at the slot `slot` and the offset `offset`.  
     ```solidity
    function set(uint256 slot, uint256 offset, bytes32 value) public
    ```
    - This function must set the value of the storage at the slot `slot` and the offset `offset` to the value `value`.

Those 2 functions must be able to get/set the value of any variables of your contract generically.

To test your implementation, try to:

- set the value of `a` to your address.
- set the second element of `mateo` to 20.
- and finally set the variable of `chall["PoC"][2]` to 999.

### :books: **Documentation**:

- [Storage layout](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html)
- [Assembly block](https://docs.soliditylang.org/en/latest/assembly.html)
- [Yul](https://docs.soliditylang.org/en/latest/yul.html)
- [EVM dialect](https://docs.soliditylang.org/en/latest/yul.html#evm-dialect)

## Conclusion

Well done ! You've accomplished a lot with this first day of P2P pool, and there is so much more to discover.
Refer to the [official documentation](https://docs.soliditylang.org/en/latest/) to deep-dive into it.

Hope you enjoyed this day !

## Authors

| [<img src="https://github.com/lucas-louis.png?size=85" width=85><br><sub>!LUK</sub>](https://github.com/lucas-louis) | [<img src="https://github.com/Nfire2103.png?size=85" width=85><br><sub>Nathan</sub>](https://github.com/Nfire2103) | [<img src="https://github.com/intermarch3.png?size=85" width=85><br><sub>Lucas Leclerc</sub>](https://github.com/intermarch3) |
| :------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------: |:------------------------------------------------------------------------------------------------------------------: |

<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white">
    </a>
</p>

> :rocket: Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.
