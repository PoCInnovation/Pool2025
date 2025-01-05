# PoC P2P Pool 2025 - Day 04 - Deployment of your NFT

**Day purposes**

✔ Save the NFT metadata on IPFS

✔ Deploy your NFT contract on the blockchain

✔ Interact with your NFT contract

✔ See your NFT in your metamask wallet

# Introduction

Today we will deploy our NFT contract from day 2 on the blockchain. We will also save the metadata of our NFT on IPFS.

# Step 1: Create and save the metadata of your NFT on IPFS

## :bookmark_tabs: **Description**:

Now that we have created our NFT, we need to save the metadata of our NFT on IPFS.

Its a littel bit long if we save them one by one by hand, so we will use a script to save them all at once.

### **Task 0: Create the metadata**

- Create a `nft_metadata` folder at the root of your project.
  - Create some json files named from 0 to 5 in the `nft_metadata` folder (`0.json`, `1.json`, ...).
  - Add the following content in each file and fill `name` and `description` with your own content:

  ```json
  {
    "name": "",
    "description": "",
    "image": ""
  }
  ```
- Create a `nft_img` folder at the root of your project.
  - Add an image for each json file in the `nft_img` folder.
  - Name the images from 0 to 5 (`0.png`, `1.png`, ...).

### **Task 1: Create the python script**

Now we will save the metadata of our NFT on IPFS. We will create a python script to do this with the `ipfs_api` package to interact with IPFS.

- Install `python` and `pip` if you don't have them installed on your computer.

- Install the `ipfs_api` package:

  ```bash
  pip install IPFS-Toolkit
  ```
- Create a python file named `save_metadata.py` at the root of your project.

### **Task 2: Save the nft img on IPFS**

In your script, you will need to do the following actions:
- count the number of files in the `img_metadata` folder.
- save each image on IPFS with the `ipfs_api`package.

### **Documentation 📚**:

- [IPFS-Toolkit documentation](https://pypi.org/project/IPFS-Toolkit/)

### **Task 3: Save the metadata on IPFS**

Now that we have saved the images on IPFS, we will save the metadata of our NFT on IPFS.
- create a `metadata` folder at the root of your project.
- count the number of files in the `nft_metadata` folder
- for each json file:
  - load the content into a json object
  - add the cid of the image to the `image` field
  - save the json object into a new file named by the name of the json file without the json extension (ex: `0.json` -> `0`) into the `metadata` folder
- save the `metadata` folder on IPFS and print the folder cid.

### ✔️ **Validation**:

Run your ipfs daemon as you learn in the previous day and then run your script. You should see the cid of the metadata folder printed in the console.

If you have correctly saved the metadata of your NFT on IPFS, you should acces to the metadata of your NFT with the following link:

```
https://ipfs.io/ipfs/<your_metadata_folder_cid>/<your_nft_id>
https://ipfs.io/ipfs/QmUggQQBL6jwfTkTqvXgDg5TxF1BWsG1vSyRnefB2HJJEa/0
```

And then in the json file returned, you should see the image cid in the `image` field.
So you should be able to access to the image with the following link:

```
https://ipfs.io/ipfs/<your_image_cid>
```

# Step 2: Deploy the NFT

## :bookmark_tabs: **Description**:

Now we will deploy our Pet NFT contracts on the [Sepolia testnet](https://www.alchemy.com/overviews/sepolia-testnet). `Sepolia` is a testnet on the Ethereum blockchain, it is a copy of the Ethereum blockchain but with fake ETH. This means that you can deploy your contracts and test them without spending real money.

- ### **Task 0: Install tools**

  - Download [Metamask](https://metamask.io) and create an account, if you don't already have one.

  MetaMask is a cryptocurrency wallet and a browser extension. It allows you to interact with the Ethereum blockchain.

  - Create your API key on [Alchemy](https://dashboard.alchemy.com/apps).
    - Sign in.
    - Click on `Create new app`.
    - Enter a name for your app and choose `NFTs` as a category.
    - Select `Ethereum` chain.
    - don't change the product access selection
    - Click on `Create app`.
    - Now, click on `Networks` and change, in `Ethereum`, Mainnet to Sepolia. you can see your RPC URL in `HTTPS`.

  Alchemy is a blockchain developer platform. It provides a set of tools to interact with the blockchain. We will use it to deploy our contracts.

  A RPC is a Remote Procedure Call, it is a protocol that allows a program to call a function on another program located on another computer. In our case, we will use it to deploy our contracts on the blockchain. We will use the `Alchemy` RPC to deploy our contracts on the `Sepolia testnet`. [Learn more about RPC here.](https://www.alchemy.com/overviews/rpc-node)

  - Go to [Sepolia faucet](https://sepolia-faucet.com/), enter your wallet address and start earning some ETH.
    - Unfortunatly to prevent from bot to drain the faucet, it's long and you can't earn ETH infinitly.
    - If you have some issue with the faucet, just ask us to send you some ETH on the discord server.

  The faucet is a website that allows you to get fake cryptocurrency, in our case, ETH on the `Sepolia testnet`. You need to have ETH to deploy your contracts.

  - Go to `MetaMask`, click on the top left corner, click on show test networks and select `Sepolia`.
  - Now you can see your balance on Sepolia.

  ## :books: **Documentation**:

  - [Sepolia documentation](https://www.alchemy.com/overviews/sepolia-testnet)
  - [MetaMask website](https://metamask.io/)
  - [Alchemy dashboard](https://dashboard.alchemy.com/apps)
  - [RPC documentation](https://www.alchemy.com/overviews/rpc-node)
  - [Sepolia faucet](https://sepoliafaucet.com/)

- ### **Task 1: Create the environment file**

  Now that we have all the tools, we need to create an environment file to store our variables needed to deploy our contracts.

  Create a `.env` file at the root of your project and add the following variables:

  ```env
  PRIVATE_KEY=
  ADMIN_WALLET=
  RPC_URL=
  CONTRACT_ADDRESS=
  ```

  - `PRIVATE_KEY` is the private key of your wallet. You can find it in `MetaMask` by clicking on the top right corner, then `Account details` and `Show private key`.
    - We use it to sign transactions and deploy contracts.
    - :warning: Never share your private key with anyone because it's the key to control your wallet.
    - For this exercise, we use a wallet with fake ETH, so it's not a problem to share it.

  - `ADMIN_WALLET` is the public address of your wallet. You can find it in `MetaMask` by clicking on the top right corner, then `Account details` and `Copy address to clipboard`.

  - `RPC_URL` is the RPC URL of `Alchemy`. Thats the url you copy in the last task.

  - `CONTRACT_ADDRESS` is the address of your contract. You will get it after deploying your contract.

  Source your environment file:

  ```bash
  source .env
  ```

- ### **Task 2: Let's deploy our contracts**

  We have now all the tools and the variables needed to deploy our contracts. Let's start to deploy our contracts. We will use [Foundry](https://book.getfoundry.sh/forge/deploying) to deploy our contracts. Foundry can be used to test contracts but also to deploy them on the blockchain.

  - Use [`forge create`](https://book.getfoundry.sh/reference/forge/forge-create) command to deploy your `PetNFTMetadata` contract with your RPC URL.

  ### ✔️ **Validation**:

  If you have correctly deployed your contract, you should see something like this:

  ```
  Deployer: 0x8F5a1Ccf3D0DE62a25bf594c14e0967fF66461DD
  Deployed to: 0x84D4606b29ee8167190B5c1eD621D9f5a4aAB43f
  Transaction hash: 0x5dffd2a389a322c7af30f8cf9bcb54713ff432bb530a2590e4966fb77598e976
  ```

  Put the address of your contract, `Deployed to`, in the `CONTRACT_ADDRESS` variable in your `.env` file.

  > :warning: Don't forget to source again your environment file.

  ### :books: **Documentation**:

  - [Foundry deploying documentation](https://book.getfoundry.sh/forge/deploying)
  - [Forge create documentation](https://book.getfoundry.sh/reference/forge/forge-create)

- ### **Task 3: Let's use our contracts**

  Congratulations! You have deployed your first contract on the blockchain. Now, we will interact with our contracts to create a pet and to feed it. To do this, we will use... Foundry again, with the [`cast`](https://book.getfoundry.sh/cast/) command.

  - Use the `cast` command to do the following actions:
    - Create a pet with the name `PoC's pet`.
    - Get your balance to verify that you have one pet.
    - Get the nft uri of the pet and verify that all is good.
    - Feed the pet.
    - Get the info of the pet to verify that its level has increased.
    - Send the pet to another wallet.

  ### :books: **Documentation**:

  - [Cast overview documentation](https://book.getfoundry.sh/cast/)
  - [Cast call documentation](https://book.getfoundry.sh/reference/cast/cast-call)
  - [Cast send documentation](https://book.getfoundry.sh/reference/cast/cast-send)

- ### **Task 4: Collect your Pet in Metamask**

  We have interacted with our contract, but we don't see our NFT. Let's add it to `MetaMask` to see it.

  - Go to `MetaMask`, click on the `NFTs` tab.
  - Click on `Import NFT`.
  - Enter the address of your contract and the id of your pet.

  You should now see your pet in `MetaMask`. Well play! You have your own NFT in your wallet.


# Conclusion

Congratulations! You have deployed your first NFT contract on the blockchain and save the metadata in a decentralized file system called IPFS. You have also interacted with it to create your first NFT. You can now create as many NFTs as you want and trade them with other people.


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

> 🚀 Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.
