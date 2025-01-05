# PoC P2P Pool 2025 - Day 02 - Create your NFT

✔️ Advance solidty notion.

✔️ Create a pet that can be minted.

✔️ Feed the pet to upgrade it.

✔️ Turn the pet into an NFT, and make it tranferable.

✔️ Add metadata to the NFT.

## Introduction

Now that you are familiar with solidity, let's build a more complex project such as creating our own NFT (Non-fungible token). If you need to learn more about NFTs, check out these links [NFT by Wikipedia](https://en.wikipedia.org/wiki/Non-fungible_token) and [NFT by Cryptoast](https://cryptoast.fr/non-fungible-token-nft-ou-token-non-fongible/).

I think by now that you are familiar with the concept of an NFT, the ability to own a unique digital asset.

If you are new to smart contract development you may think that an NFT is a complex piece of code but in reality it is a program running on a blockchain. Just as any other contract.

First, you may wonder : what will this NFT do ?

We will create an NFT representing a Pet. It can be minted (created) by any wallet and be fed to upgrade its level. To feed a Pet, you will need to pay a certain price.

## Step 0 - Setup

Please refer to the [SETUP.md](./SETUP.md) file, it is the same as the previous day.

## Step 1: Pet Factory Contract

### :bookmark_tabs: **Description**:

Let's start by creating a contract which:

- Makes every user able to mint (create) a pet
- Stores each user's ownership of their pets

Each pet must have a:

- Name
- Id
- Level
- Feed time

### :pushpin: **Tasks**:

- ### **Task 0: Init the contract**

  Let's start by creating a file in `src` called `PetFactory.sol`.

  Add these lines at the top of your file:

  ```solidity
  // SPDX-License-Identifier: MIT
  pragma solidity ^0.8.20;
  ```

  And create the contract `PetFactory`.

  In this contract create a `struct` `myPet` which contains a:

  - `name` which corresponds to the pet name
  - `level` which corresponds to the pet level
  - `toFeed` which corresponds to the time when the pet will be able to be fed (timestamp)

  To make work the contract, we need also a:

  - `uint8` called `cooldownTime` which is set to `1 minutes`.
  - `array` of `myPet` called `_myPets`.
  - `mapping` with key `uint256` (the pet's id) and value `address` called `_owners` to know who is the pet owner.
  - `mapping` with key `address` (owner address) and value `uint256` called `_petCount` to keep track of how many pet are owned by a person.

  > :warning: Becareful about the visibily of the variables

  If you encounter difficulties creating variables, you can go back and take a look at [Step 4](../day01/README.md#step-4---variables-types-2) of Day1.

- ### **Task 1: Create Pet**

  Now that we created the contract, we need to add a function to call to mint (create) a pet and return its id. This function will be limited to be only called five times per wallet (if the wallet already own five pets, they can't get a new pet).

  Here is the expected function's prototype:

  ```solidity
  function _createPet(string memory _name) internal returns (uint256) {}
  ```

  At the beginning of this function, you need to use `require` to check if the owner has less than five pets and if the pet already exists.

  When creating a pet set its `level` to `1`, and its `toFeed` attribute to the `current timestamp`.

  > 💡 Don't forget to update the mappings :grin:

  ### :books: **Documentation**:

  - [Array example](https://solidity-by-example.org/array)
  - [Mapping example](https://solidity-by-example.org/mapping)
  - [Require example](https://solidity-by-example.org/error)
  - [Timestamp documentation](https://docs.soliditylang.org/en/latest/units-and-global-variables.html#block-and-transaction-properties)

- ### **Task 2: Get info**

  Now that we are able to create a Pet, we need one method to view who owns which pet, a second one to view which pet we currently own and a third one to get my pet's info.

  Implement a function called `getPetsIdFromAddress` which returns an array of the indexes of pets owned by a giving adress.

  ```solidity
  function getPetsIdFromAddress(address _owner) public view returns (uint256[] memory) {}
  ```

  Implement a function called `getMyPetsId` which returns an array of the indexes of pets owned by the caller of the function.

  ```solidity
  function getMyPetsId() public view returns (uint256[] memory) {}
  ```

  Implement a function called `getMyPet` which returns my pet's info.

  ```solidity
  function getMyPet(uint256 _petId) public view returns (myPet memory) {}
  ```

  > :warning: Don't forget to check if the pet is yours.

- ### **Task 3: Testing**

  Let's test our contract. For testing our contracts we will use [Foundry](https://book.getfoundry.sh/forge/writing-tests), like we did in the previous day. If you encounter difficulties creating tests, you can go back and take a look at [Step 6](../day01/README.md#step-6---testing-with-foundry) of Day1.

  - Create a new file `PetFactory.t.sol` in the `test` folder.
    - This file will contain the tests of your smart contract.
  - Create a contract `PetFactoryTest` inherit from `Test` contract.
    - You have to import `Test` contract, this one is contained in lib/forge-std folder.
  - Create a `setUp` function which will be executed before each test.
    - Call your smart contract in this one.
  - Create the next functions to test your smart contract:
    - `testCreatePet` : This function will test the function `_createPet`.
    - `testCreatePetIfCallerHasAlreadyFivePets` : This function will test the function `_createPet` if the caller has already five pets.
    - `testGetMyPetIfCallerIsNotTheOwner` : This function will test the function `getMyPet` if the caller is not the owner of the pet.
    - `testGetMyPetsId` : This function will test the function `getMyPetsId`.
  - Execute the command [`forge test`](https://book.getfoundry.sh/reference/forge/forge-test) to run the tests.
    - You can use `forge test -vvvv` to show more information.

  > 💡 You can create contract helper to call internal variables or functions.
  > 💡 Take a look at the vm.startPrank() and vm.expectRevert()

  It is very important to test correctly your smart contract, because when it is deployed on the blockchain, you can't modify it. If you have a bug in it, you can't fix it. That's why it is important to test every case and every line of your smart contract.

  ### :books: **Documentation**:

  - [Foundry testing documentation](https://book.getfoundry.sh/forge/writing-tests)
  - [Forge test documentation](https://book.getfoundry.sh/reference/forge/forge-test)
  - [Test internal fonction](https://book.getfoundry.sh/tutorials/best-practices#test-harnesses)
  - [Start prank](https://book.getfoundry.sh/cheatcodes/start-prank)
  - [Expect revert](https://book.getfoundry.sh/cheatcodes/expect-revert)

## Step 2: Feeding Contract

### :bookmark_tabs: **Description**:

Now let's feed our pet. When a user will want to feed his pet, the user will have to pay a certain amount to be able to feed the pet.

### :pushpin: **Tasks**:

- ### **Task 0: Init the contract**

  Let's start by creating a new contract, create a new file called `PetFeeding.sol` and create the contract called `PetFeeding`.

  Add these lignes at the top of your file:

  ```solidity
  // SPDX-License-Identifier: MIT
  pragma solidity ^0.8.20;
  ```

  Your contract will have to inherit the contract `PetFactory` to have access to the previous contract.

  We need a `uint256` called `levelFee` which is set to `0.000001 ether`, this fee will be the price each user must pay to upgrade their pet.

  ### :books: **Documentation**:

  - [Inheritance documentation](https://docs.soliditylang.org/en/latest/contracts.html#inheritance)
  - [Inheritance example](https://solidity-by-example.org/inheritance/)

- ### **Task 1: Feed a Pet**

  We now need to create a function to feed our pet. As said in the introduction, the user will need to pay a fee to feed his pet.

  Below is the function's prototype:

  ```solidity
  function feedMe(uint256 _petId) external payable onlyPetOwner(_petId) {}
  ```

  As you can see, we use the `payable` keyword indicating that the calling the function will trigger a payment.

  We also have `onlyPetOwner(_petId)` which is a `modifer` that you are going to write, in the `PetFactory` contract.

  ```solidity
  modifier onlyPetOwner(uint256 _petId) {}
  ```

  Quick remember: `Modifier` is an element that will check if it can execute the function.\
  For example, check if the pet belongs to the one who wants the feed. :eyes:

  Don't forget to check if the pet can be fed (by checking its `toFeed` variable), and if the user has payed the right amount with `require`.

  If the pet can be fed, raise its level by one, and change the `toFeed` variable to the `current time` + `cooldownTime` (defined in `PetFactory.sol`).

  Your turn :grin:

  ### :books: **Documentation**:

  - [Modifier documentation](https://docs.soliditylang.org/en/latest/contracts.html#function-modifiers)
  - [Modifier example](https://solidity-by-example.org/function-modifier/)
  - [Payable documentation](https://cryptomarketpool.com/payable-modifier-in-solidity-smart-contracts/)

- ### **Task 2: Change the feeding price**

  There is an issue with our implementation: that the price to feed a pet is constant. This means that if you want to change the price, you need to upload a new contract with the new value. If your contract needs to last on the long term on the blockchain, you need to be able to change values, such as the price.

  Create a function to set a new value to `levelFee`:

  ```solidity
  function setPrice(uint256 _levelFee) external {}
  ```

- ### **Task 3: Role based contract**

  This function works fine but a big problem is that anyone can call this function and they can set the price to zero. This isn't the desired behaviour. Only the contract owner should be able to change the price to feed a pet.

  Create the following modifier, and apply it on `setPrice`:
  The contract owner is the one who deployed the contract.

  ```solidity
  modifier onlyContractOwner() {}
  ```

  ### :books: **Documentation**:

  - [Modifier documentation](https://docs.soliditylang.org/en/latest/contracts.html#function-modifiers)
  - [Modifier example](https://solidity-by-example.org/function-modifier/)

- ### **Task 4: Testing**

  It's time to test our contract. Let's testing our contract like we did in the previous step.

  - Create a new file `PetFeeding.t.sol` in the `test` folder.
  - Create a contract `PetFeedingTest` inherit from `Test` contract.
  - Create the next functions to test your smart contract:
    - `testFeedMe` : This function will test the function `feedMe`.
    - `testFeedMeIfCallerIsNotTheOwner` : This function will test the function `feedMe` if the caller is not the owner of the pet.
    - `testFeedMeNotEnoughMoney` : This function will test the function `feedMe` if the caller doesn't have enough money to feed the pet.
    - `testFeedMeCanNotBeFeed` : This function will test the function `feedMe` if the pet can't be feed right now.
    - `testSetPrice` : This function will test the function `setPrice`.
    - `testSetPriceIfCallerIsNotTheOwner` : This function will test the function `setPrice` if the caller is not the owner of the contract.
  - Execute the command `forge test` to run the tests.

  > 💡 Think to test every case and every line of your smart contract.

  ### :books: **Documentation**:

  - [Foundry testing documentation](https://book.getfoundry.sh/forge/writing-tests)
  - [Forge test documentation](https://book.getfoundry.sh/reference/forge/forge-test)

## Step 3: Pet NFT Contract

### :bookmark_tabs: **Description**:

Until now we haven't really used the word NFT to describe the pet, we could have described it as an NFT because a pet can only be owned by a single wallet, thus it's **non-fungible**. But we aren't able to transfert it, this is a main feature of an NFT, it can be sent and exchange between wallets.

Your next step is to create a contract which makes possible for wallets to transfert pet and to approve a transaction.

Approving a transaction means that you approve a given wallet to transfer your pet to himself at any time, unless if you remove the approval.

### :pushpin: **Tasks**:

- ### **Task 0: Init the contract**

  Let's start by copying the `IERC721.sol` file in your `src` folder, we will detail its usefulness later.

  Continue by creating a contract called `PetNFT`.

  Add these lignes at the top of your file:

  ```solidity
  // SPDX-License-Identifier: MIT
  pragma solidity ^0.8.20;
  ```

  Your contract will have to inherit the contract `PetFeeding`, and `IERC721`.

  You may have seen the `IERC721.sol` file from the start of the day. `ERC721` is the technical name for an NFT contract. This contract contains an `interface`. It is the skeleton of a contract, it contains the function prototype which much be implemented in the contract.
  [Learn more about ERC721 here.](https://eips.ethereum.org/EIPS/eip-721)

  ### :books: **Documentation**:

  - [Interface documentation](https://docs.soliditylang.org/en/latest/contracts.html#interfaces)
  - [Interface example](https://solidity-by-example.org/interface/)
  - [Inheritance documentation](https://docs.soliditylang.org/en/latest/contracts.html#inheritance)
  - [Inheritance example](https://solidity-by-example.org/inheritance/)

- ### **Task 1: Copy prototypes**

  To simplify implementation, we will copy the prototypes of the functions from `IERC721.sol` to `PetNFT.sol`. Replace `external` visibility with `public` visibility and add the `override` keyword.

  ### :books: **Documentation**:

  - [Visibility documentation](https://docs.soliditylang.org/en/latest/contracts.html#visibility-and-getters)
  - [Override documentation](https://docs.soliditylang.org/en/latest/contracts.html#function-overriding)

- ### **Task 2: Implement basics function**

  We have now the prototypes of the functions, we need to implement them. Let's start with the `balanceOf` and `ownerOf` functions.

  ```solidity
  function balanceOf(address owner) public view override returns (uint256)
  ```

  This function returns the number of ERC721 tokens owned by the given address.

  ```solidity
  function ownerOf(uint256 tokenId) public view override returns (address)
  ```

  This function returns the address that owns the given ERC721 token.

  > :warning: Don't forget to check if the token exists.

- ### **Task 3: Implement approve functions**

  We now need to implement the `setApprovalForAll`, `isApprovedForAll`, `approve` and `getApproved` functions. These functions are used to approve a transaction. It means that you approve a given wallet to transfer your pet to himself at any time, unless if you remove the approval.

  ```solidity
  function setApprovalForAll(address operator, bool approved) public override
  ```

  👆 This function allows the owner of an ERC721 token to approve or remove the approval of another address to transfer all their tokens on their behalf.

  ```solidity
  function isApprovedForAll(address owner, address operator) public view override returns (bool)
  ```

  👆 This function returns if the given operator is approved to transfer all the tokens of the given owner.

  ```solidity
  function approve(address to, uint256 tokenId) public override
  ```

  👆 This function allows the owner of an ERC721 token to approve another address to transfer the token on their behalf.

  ```solidity
  function getApproved(uint256 tokenId) public view override returns (address)
  ```

  👆 This function returns the address that was approved for the given ERC721 token.

  > 💡 For these implementations we need to implement two mappings.

  > :warning: Don't forget to take a look of the requirements of each function. Look at the comments on top of each function to know what they do and what event they need to emit.

- ### **Task 4: Implement transferFrom function**

  Finally, we now need to implement the `transferFrom` function. This function is used to transfer a pet from one wallet to another.

  ```solidity
  function transferFrom(address from, address to, uint256 tokenId) public override
  ```

  This function allows the owner of an ERC721 token to transfer the token to another address.

  > :warning: Don't forget to take a look of the requirements of this function.

- ### **Task 5: Implement mint function**

  We have now implemented all the functions from the `IERC721.sol` file. But we still need to implement the `mint` function to create a new ERC721 token (a new pet).

  ```solidity
  function mint(string memory name) public
  ```

  This function allows the caller of the function to mint a new token.

  > 💡 We have already implemented a function to create a pet in the `PetFactory.sol` file, you can use it.

  > :warning: Don't forget to emit the `Transfer` event.

- ### **Task 6: Testing**

  Before deploy our contract on the blockchain, we need to test it. Let's testing our contract like we did in the previous steps. This time, I don't help you, you need to create the tests by yourself. Just keep in mind that you need to test every case and every line of your smart contract.

  > 💡 Don't forget to test event emitted.

  ### :books: **Documentation**:

  - [Foundry testing documentation](https://book.getfoundry.sh/forge/writing-tests)
  - [Forge test documentation](https://book.getfoundry.sh/reference/forge/forge-test)
  - [Expect emit documentation](https://book.getfoundry.sh/cheatcodes/expect-emit)

## Step 4: Pet NFT Metadata Contract

### :bookmark_tabs: **Description**:

Now to be able to link metadata to our NFT like an image we need to add some functions. An NFT metadata is a file which contains information about the NFT. It can be the name, the image, the description, etc. This file is stored on a server and can be accessed by a link. This link is stored in the smart contract.

For today you will use some metadata i have already uploaded on `IPFS`. `IPFS` is a protocol and a peer-to-peer network for storing and sharing data in a distributed file system. [Learn more about IPFS here.](https://docs.ipfs.io/concepts/what-is-ipfs/)
You will learn more about IPFS during the next days.

Let's add metadata to our NFTs to be able to see the name and the image of our pets.

- ### **Task 0: Init the contract**

  Let's start by copying the `IERC721Metadata.sol` file in your `src` folder, we will detail its usefulness later.

  Continue by creating a contract called `PetNFTMetadata`.

  Add these lignes at the top of your file:

  ```solidity
  // SPDX-License-Identifier: MIT
  pragma solidity ^0.8.20;
  ```

  Your contract will have to inherit the contract `PetNFT`, and `IERC721Metadata`.

  You may have seen the `IERC721Metadata.sol` file from the start of the day. `ERC721Metadata` is the interface which contains the function prototype to get the metadata of an ERC721 token.

- ### **Task 1: Named our NFTs**

  Let's start by named our NFTs.

  - Create the following variables with the correct visibility:
    - `name`: which corresponds to the name of your NFT collection.
    - `symbol`: which corresponds to the abbreviation of the name.
    - `_baseURI`: which correspond to the base link of the nft metadata (an IPFS link in our case).
      - Set its value to the base CID of the metadata. (Ask me for the CID of the metadata i have already uploaded on IPFS)
      The base URI of the metadata is a link like this `ipfs://QmVmTDg5sNBtt62r3ksQBKHVZK9mqJ4sH4Vyfgd6c3KDL9/`

- ### **Task2: Implement the link of the metadata**

  We now need to implement the `tokenURI` function. This function returns the link of the metadata of the ERC721 token.

  ```solidity
  function tokenURI(uint256 tokenId) public view override returns (string memory)
  ```

  You need to concatenate the base URI with the id of the token.

  In case the URI need to be changed, implement a function to change it: 
  ```solidity
  function setBaseURI(string calldata newURI) external
  ```

  > ⚠️ Only the Owner of the contract can change the URI

- ### **Task 3: Implement supports interface**

  In order that an application can know if the contract supports the `ERC721Metadata` interface, we need to implement the `supportsInterface` function. This function returns if the contract supports the given interface.

  ```solidity
  function supportsInterface(bytes4 interfaceId) public pure returns (bool)
  ```

  This function must return `true` if the interfaceId corresponds to the `ERC721` or `ERC721Metadata` interface.

  > 💡 You can use type(Interface).interfaceId to get the interfaceId of an interface.

- ### **Task 4: Testing**

  Let's test our contract, like we did in the previous step I don't help you, you need to create the tests by yourself. Just keep in mind that you need to test every case and every line of your smart contract.

  ### :books: **Documentation**:

  - [Foundry testing documentation](https://book.getfoundry.sh/forge/writing-tests)
  - [Forge test documentation](https://book.getfoundry.sh/reference/forge/forge-test)

## Conclusion

Congratulations! You have created your first NFT. You have learned how to create an NFT with its metadata. You will learn how to deploy it with it's metadata during the next days.

## Authors

| [<img src="https://github.com/MrSIooth.png?size=85" width=85><br><sub>Victor</sub>](https://github.com/MrSIooth) | [<img src="https://github.com/Alex-Prevot.png?size=85" width=85><br><sub>Alex</sub>](https://github.com/Alex-Prevot) | [<img src="https://github.com/Doozers.png?size=85" width=85><br><sub>Isma</sub>](https://github.com/Doozers) | [<img src="https://github.com/Nfire2103.png?size=85" width=85><br><sub>Nathan</sub>](https://github.com/Nfire2103) | [<img src="https://github.com/intermarch3.png?size=85" width=85><br><sub>Lucas Leclerc</sub>](https://github.com/intermarch3) |
| :--------------------------------------------------------------------------------------------------------------:  | :------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |

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
