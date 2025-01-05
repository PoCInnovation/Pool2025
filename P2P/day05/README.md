# PoC P2P Pool 2025 - Day 05 - PoC Ether

✔️ Learn with a CTF challenge.

✔️ Learn about the Ethereum blockchain.

✔️ Advance solidty notion.

## Introduction

Today, we will be learning with the help of a CTF challenge. It's a nice way to learn new things and to practice what we have learned so far. This is the link to the challenge: https://ether.poc-innovation.com/  

This platform is a CTF challenge about smart contracts created by the PoC Innovation team. The goal is resolve the challenge by interacting with the contract to attack.

When you click on the link, your browser wallet will ask to connect a wallet to the website. Choose the wallet you have created during this week with fake ETH on the Sepolia testnet.

## Step 1 : Understand the plateform

Go to the Help page and read the instructions. You will find the rules of the game and the different steps to follow to solve the challenge.

## Step 2 : Choosing a level

Go to the Challenges page and choose a level to start with. You will see a list of levels with different difficulties. Choose the first level.
Now you can see the level title, the goal of the level and the contract code to attack.

## Step 3 : Start a level instance

Open the console of your browser.
Click on the `Get a New Instance` button.
Now the level title and the contract code are displayed in the console (wait a bit for the contract to be deployed on the blockchain).

## Step 4 : Attack the contract

Now that the contract is deployed, you can start attacking it. You can interact with the contract by calling its functions.
When you think you have found the solution, click on the `Validate Instance` button to validate your answer and the website will tell you if you have succeeded or not.

## Step 5 : Become a solidity master

Repeat the previous steps with the other levels to become a solidity master.

## Example with the first level

Here is an example of how to solve the first level:
```solidity
contract BecomeTheOwner {
    address public owner;

    constructor() public {
        owner = msg.sender;
    }

    function becomeTheOwner() public {
        if (tx.origin == msg.sender) {
            owner = msg.sender;
        }
    }
}
```

Here we want to become the owner of the contract by setting the `owner` variable to our wallet address. As you can see, their is only one function `becomeTheOwner` that can be called by anyone.
In it we have a condition that checks if the `tx.origin` is equal to the `msg.sender`.
The `tx.origin` is the original sender of the transaction, it is the address of the wallet that initiated the transaction.
The `msg.sender` is the address of the wallet/contract that called the function.
So if the `tx.origin` is equal to the `msg.sender`, we can call the function and become the owner of the contract.
So we just need to call the function with our wallet and become the owner of the contract.

> **Note**: For this challenge you just need to interact with the contract by calling its functions from your wallet. You don't need to deploy any contract but for most of the challenges you will need to deploy a contract that will interact with the challenge contract to solve it.

Don't hesitate to ask for help if you are stuck with the plateform or anything else.
I you are **really** stuck with a level **for a long time**, you can ask for help for an hint to help you solve it but try to solve it by yourself first.

## Conclusion

This challenges is a good way to practice what we have learned so far. It will help you to understand how to interact with a contract and how to attack it. It will also help you to understand the different vulnerabilities that can be found in a contract.
I hope you will enjoy this challenges and that you will learn a lot from it.


## Authors

| [<img src="https://github.com/intermarch3.png?size=85" width=85><br><sub>Lucas Leclerc</sub>](https://github.com/intermarch3) | [<img src="https://github.com/lucas-louis.png?size=85" width=85><br><sub>Lucas Louis</sub>](https://github.com/lucas-louis) | [<img src="https://github.com/0xtekgrinder.png?size=85" width=85><br><sub>0xtekgrinder</sub>](https://github.com/0xtekgrinder) | [<img src="https://github.com/AbdelkarimBENGRINE.png?size=85" width=85><br><sub>Abdelkarim Bengrine</sub>](https://github.com/0AbdelkarimBENGRINE) | [<img src="https://github.com/Nfire2103.png?size=85" width=85><br><sub>Nathan Flattin</sub>](https://github.com/Nfire2103) |
| :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |

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

> 🚀 Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.




