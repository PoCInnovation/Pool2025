# PoC Software Pool 2025 Day 05 - Svelte

**Day purposes**

✔ Create your own User Interface (UI) with Svelte and Flowbite Svelte ✨

✔ Structure your UI 🚧

✔ Test your UI 🧑‍💻

## Introduction

*[Svelte](https://svelte.dev/) is a Javascript library to build user interfaces.*

**What is a user interface?**

A user interface (UI) is the point at which humans interact with a computer, a website or an application. 💻

For instance, your terminal is a user interface.

**What does this Javascript library allow us to do?**

Thanks to Svelte, you can build [components](https://svelte.dev/docs/svelte-components). A component is a Javascript function that returns a Javascript object representing a DOM element in memory.

> 💡 DOM stands for Document Object Model, which is the HTML representation of a web page. As a consequence, a DOM element is a part of the HTML representation of a web page.

However, unlike [React](https://en.reactjs.org/), Svelte doesn't rely on a virtual DOM to update the actual DOM. Instead, it compiles your components into optimized Javascript code. This approach makes the rendering of your app more efficient. 🚀

> The real DOM is the HTML representation of the web page that the user sees. It's updated by [queries](https://burlingtoncodeacademy.github.io/webdev-prework-track/DOM_queries). The virtual DOM is a copy of the real DOM.

<div align="center">
<img src="https://images.prismic.io/superpupertest/11ea057c-1c4b-42aa-a79b-f5fd4e49f8d0_pic.webp?auto=compress,format&w=680&h=446.760&dpr=3" />
</div>

## Step 0 - Setup

### :pushpin: **Tasks**:

- In your pool repository, create a new directory for the `day05`:

```sh
mkdir -p day05
```

- Then, create a new Svelte project with Typescript:

```shell
npm create vite@latest artists-book -- --template svelte-ts
```

- To verify that everything is ok, run the following commands:

```shell
# Move to your project
cd artists-book

# Install the required dependencies
npm install

# Start the server
npm run dev
```

If you get a page with the Vite and the Svelte logos, then you can continue 🚀

## Step 1 - Lay the foundations

Before starting the tasks, let's prepare your project.

Install all the packages we're going to use for this day:

```sh
npm i svelte-routing cypress flowbite flowbite-svelte
```
### :bookmark_tabs: **Description**:

You'll build your UI with [Flowbite Svelte](https://flowbite-svelte.com/), which is a component library for Svelte.

Now that the foundations are laid for your project, it's time to dive into frontend development 🏊

## Step 2 - Your first component 🚀

### :bookmark_tabs: **Description**:

Let's start by creating the Home page 😄 

### :pushpin: **Tasks**:
- Create the file `src/pages/Home.svelte` with a Svelte component representing your Home page inside.
  It must contain:
  - a title `Artists Book` 🧑‍🎤
  - a subtitle `Manage your favorite artists` ⭐
- Update the file `src/app/App.tsx` to call this component.

> Remove the initial content of ```src/App.svelte``` to start off fresh.

### :books: **Documentation**:
- Check [what a Svelte component is made of](https://svelte.dev/docs/svelte-components) 👀
- Take a look-up at the [Heading](https://flowbite-svelte.com/docs/typography/heading) component in Flowbite Svelte 😉

### ✔️ **Validation**:
![Task 2 Preview](previews/task2-preview.png)

Well done! You have created your first Svelte Component 🥳

> 💡 A **great idea** is to create a folder `src/components` to store reusable components.

## Step 3 - Your first routes 🛤️

### :bookmark_tabs: **Description**:
Now that you have your Home page, it's time to have Register and Login pages reachable at the `/register` and `/login` URLs 😉

### :pushpin: **Tasks**:
- Create the `src/pages/Register.svelte` file, which will contain the Register page.
It must contain:
  - An `Input` to enter an `email`.
  - An `Input` to enter a `password`.
  - An `Input` to enter the `confirmed password`.
    > 💡 Text for the password inputs mut be replaced by dots
  - A `Button` that when clicked, log the values of the email, the password and the confirmed password.

- Create the `src/pages/Login.svelte` file, which will contain the Login page.
  - An `Input` to enter an `email`.
  - An `Input` to enter a `password` with text replaced by dots again.
  - A `Button` that when clicked, log the values of the email and the password.
  - A `Button` to the Register page.

- Create the `src/app/Routes.svelte` file, with a Svelte component containing the Routes inside, called in `src/App.svelte`.

- Finally, update the home page, by adding:
  - A `Button` to the Register page.
  - And a `Button` to the Login page.

### :books: **Documentation**:
- Have a look at the Flowbite Svelte [Button](https://flowbite-svelte.com/docs/components/buttons) and [Input](https://flowbite-svelte.com/docs/components/forms#mainContent) components. 
- Take also a look at the [svelte-routing](https://github.com/EmilTholin/svelte-routing) package.
- As well, check out what [binding](https://svelte.dev/docs/element-directives#bind-property) is in Svelte (that might be useful for the inputs  👀)

### ✔️ **Validation**:
![Task 3 preview homepage](previews/task3-preview-homepage.png)
*The home page.* 🏠

![Task 3 preview login page](previews/task3-preview-login-page.png)
*The login page.*

![Task 3 preview register page](previews/task3-preview-register-page.png)
*The register page.*

## Step 4 - Testing time 🧪

### :bookmark_tabs: **Description**:
Great, you now have a nice UI, but how do you make sure it works well without manually testing?

A great tool for front-end testing is [Cypress](https://www.cypress.io/), mainly used for [end-to-end](https://css-tricks.com/front-end-testing-is-for-everyone/#h-end-to-end-e2e-testing) and [component](https://docs.cypress.io/guides/component-testing/overview) tests.

To win time, we already created some tests for you, you'll just need to adapt them to your application 😄

### :pushpin: **Tasks**:

- Since we've installed Cypress earlier, you can just add the necessary scripts in the `package.json`:
```json
"cypress:run": "cypress run",
"cypress:open": "cypress open",
```
> You can run the tests directly in the CLI or open a UI to do so 😉

- Once this is done, [extract the given files](./src/svelte-tests.zip). You should have a `cypress` folder at the root of your project with the test files located in `cypress/e2e`, and a `cypress.config.ts` file also at the root.
> 💡 You'll notice the `cypress/videos` and `cypress/screenshots` folders, when you run the tests cypress will fill these directories with content to help you debug your tests if they fail. You can add them to your `.gitignore` to avoid committing them. 

- Lastly, you will need to add some [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id?retiredLocale=id) to the components of your UI. They will be useful to find content of your UI, especially here for the cypress tests. 

For example in `home.cy.ts`, you have this test for the title where we find the UI content based on the `app-title` id:
```ts
it('Good title', () => {
  cy.get('#app-title').should('contain', 'Artists Book');
});
```

When you're done, you can use `npm run cypress:run` and admire the passing tests 🚀

> During the next steps, feel free to add tests for the new components and pages you create 😉

## Step 5 - Your first dashboard 📋

### :bookmark_tabs: **Description**:
Now that you have solid foundations, it's time to go further 🔥

You have a Home page, a Register page and a Login page. What's missing? A Dashboard page!

Let's now play with artists 🚀

> 💡 To see what is an `Artist`, check the [API doc](../resources/README.md)

### :pushpin: **Tasks**:

- Create the `src/pages/Dashboard.svelte`. It will contain the Dashboard page listing some artists, with the `/dashboard` URL.
  The Dashboard page must contain:
  - A `Navbar` in the top with:
    - A `Link` to the Dashboard page on the left.
    - A `Button` `Add an Artist` on the right, **doing nothing for now**.
  - A `Gallery` listing artists `card`.

> ⚠️ For now, data is stored within the component. There is no real database and no interaction with the API.

- Update the Register `Button` to redirect to the Dashboard page when clicked.
- Update the Login `Button` to redirect to the Dashboard page when clicked.
- Add the following files:
    - `src/types/artist.ts` with the `Artist` type inside. Be smart, take only the needed properties 😎
    - `src/components/Bar/TopBar.svelte` with the top `Navbar` inside.
    - `src/components/Button/AddArtistButton.svelte` with the `Add an Artist` `Button` inside.
    - `src/components/Card/ArtistCard.svelte` with the artists `card` inside, displaying every information about an artist except from his `id`.
    > Try to display the `rating` using 5 stars ⭐

### :books: **Documentation**:
- The Flowbite Svelte [Gallery](https://flowbite-svelte.com/docs/components/gallery#mainContent), [Navbar](https://flowbite-svelte.com/docs/components/navbar), [Link](https://flowbite-svelte.com/docs/typography/link]) and [Rating](https://flowbite-svelte.com/docs/components/rating) components will be useful for this dashboard 😉

### ✔️ **Validation**:
![Task 5 preview Dashboard](previews/task5-preview.png)
*The Dashboard page.*

## Step 6 - Become a true Frontend Developer 📈

### :bookmark_tabs: **Description**:
Now that you can list artists, what if you could add some?

As you can notice, your `Add an artist` button does nothing for now.

Let's add artists in a cool way 😎: when this button is clicked, a `Modal` appears with a form to create an artist.

### :pushpin: **Tasks**:
- You must create the file `src/components/Modal/AddArtistModal.svelte` with the `Modal` to add an artist inside, called in `src/components/Button/AddArtistButton.svelte`

### :books: **Documentation**:
- Flowbite Svelte has a component perfectly fit for this use case: the [Modal](https://flowbite-svelte.com/docs/components/modal#mainContent) 🔥

### ✔️ **Validation**:
![Task 6 preview modal add an artist](previews/task6-preview-add-artist.png)
*Modal to add an artist.*

***
### **⚠️ Important note ⚠️**

First, well done! You've worked hard to be here 👏

It's time to give you a gift: one advice 🎁

One of the most difficult thing when you build a User Interface with React (and other libraries of components / frameworks) is to manage the dozens of components you create.

But why is it difficult?

It's because your components are not **stateless**. ***There is logic inside them***. For instance, sometimes you will copy-paste a whole component, just to change a condition, a function...

It's really difficult to build components that you can re-use in different parts of your project.

So how can you resolve this problem?

One of the best thing to do is to build ***stateless components***.

Keep your logic, your function calling APIs... the higher in your tree component. Pass functions, conditions... ***as parameters*** to your components.

It might not seem important right now, but it will help you so much.

To set this up, here is a little challenge you can take: all your logic, keep it inside the pages components, and only there.

If you want to go further in frontend development, follow this principle as much as you can 😉
***

## Step 7 - Implement stores 🏪

### :bookmark_tabs: **Description**:
However, when you want to add an artist, you'll find out that the Dashboard isn't updated. It's because the array where you store your `Artists` is shared between multiple components. In order to fix this, let's implement stores! 😄 

A store is an object with a subscribe method, that allows interested parties (such as components) to be notified whenever the store value changes. Thanks to stores, you can share data between different components without passing parameters to them.

Here, we want to create a store for the `Artists` list of the `Dashboard`, so that whenever we add a new `Artist`, the Dashboard updates!

### :pushpin: **Tasks**:
- Create the `src/stores/Artists.ts` file, where you'll define the `artists` store.
- Add the `susbscribe` method in `src/pages/Dashboard.ts`, in order to update the list of `Artists` whenever `artists`'s value is updated.
- Change the way you're updating the list of `Artists` in `src/components/Modal/AddArtistModal.svelte`.

### :books: **Documentation**:
- Learn about stores [here](https://svelte.dev/docs/svelte-store) 👍

### ✔️ **Validation**:
![Step 7 preview](previews/task7-preview.png)
*The Dashboard page after adding a new artist.*

## Step 8 - Your first API call from a UI 💯

### :bookmark_tabs: **Description**:
Now that you have built your User Interface, it's time to call the [API](../resources/README.md) and interact with real data 🚀
> Please take a moment to set up this.\
> Feel free to play with it with a tool like [Postman](https://www.postman.com/) or [Insomnia](https://www.insomnia.rest/).

Let's call the API when a user registers 🧔‍♂️

### :pushpin: **Tasks**:
- Create functions that will call the API, inside the folder `src/services`. In your Svelte components, you will call these functions. Be smart, you're free to organize this folder as you want.
  - These functions must:
      - Notify the user with the appropriate message if the register action succeeds or fails.
      - Make the Register button not clickable if the credentials are invalid.
      - Redirect the user to the Dashboard page, on success.
- You must have an [env variable](https://vitejs.dev/guide/env-and-mode) `VITE_APP_BACKEND_URL`.
- You must get the `VITE_APP_BACKEND_URL` inside the file `src/config/services.ts`, and only here.

### :books: **Documentation**:
- Have a look at the [axios](https://www.npmjs.com/package/axios) package.
- Another step, another Flowbite UI component! This time, look at the [toast](https://flowbite-svelte.com/docs/components/toast) component. (And its associated [icons](https://flowbite-svelte.com/docs/extend/icon)).
- Take a look at the [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), this is where you can keep the `accessToken`. Try to mix it up with Svelte stores to have more control over this !

***
### **⚠️ Important note ⚠️**

You will store the given `accessToken` inside the `localStorage`.

Note that this is a **bad idea**.
> Please refer to [the Security Bonus](#security-issue) to understand why.

We ask you to do it this way because it's important to be aware of this.
***

## Step 9 - Time to play with real data 🚀

### :bookmark_tabs: **Description**:
Now that you know how to call an API from a User Interface, it's time to have a complete interaction with it!

### :pushpin: **Tasks**:
- Update your code to follow the next requirements:
  - On successful login, the user must be redirected to the Dashboard page.
  - The user must be notified with the appropriate message on login.
  - The user must be authenticated on the Dashboard page. If not, redirect him to the Home page.
  - The user must be notified with the appropriate message on artist creation.
- Don't forget to structure your code.
  
You already have all you need, but you can ask the staff if you struggle 😄

## Step 10 - What about musics? 🎶

### :bookmark_tabs: **Description**:
Well, we have artists. What about musics?

Let's create an Artist page listing all of his musics. 🎵

### :pushpin: **Tasks**:
- Create the `src/pages/ArtistPage.svelte` file, with the Artist page. It must contain:
  - The same top `navbar` as the Dashboard page.
  - The photo / name / rating / nationality / music gender of the artist, displayed in a nice way.
  - An `Add a music` `button` opening a `modal` to add a music when clicked.
  - A `grid` listing his music's `card`.
  - When an artist is created, redirect the user to this artist's page.
- Create the following files:
  - `src/components/Card/MusicCard.svelte` with the musics `card` inside, displaying every information about a music except from its `id`.
  - `src/components/Button/AddMusicButton.svelte` with the `Add a Music` `button` inside.
  - `src/components/Modal/AddMusicModal.svelte` with the `modal` to add a music inside, called in `src/components/Button/AddMusicButton.svelte`.
  
This is not the time to optimize your number of requests to the API. Keep it logical.

## Bonus

Congratulations on completing this day, you're now able to create a beautiful frontend for your own project 🤩

Here are some bonuses for you if you still have time:

### SvelteKit

Take a look at [SvelteKit](https://kit.svelte.dev/), an app framework built on top of Svelte, which allows developers to build full-stack applications with Svelte.

### Dark & Light Mode

Implement a Dark and Light Mode thanks to [Flowbite](https://flowbite-svelte.com/docs/components/darkmode) 🕶️

### Security Issue

As stated earlier, storing a JWT inside the `localStorage` is a bad idea. Here is [how to solve this problem](https://www.codeheroes.fr/2020/06/20/securiser-une-api-rest-3-3-gestion-du-jwt-cote-client/) 😉

Your turn!

<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn logo">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram logo"
>
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter logo">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord logo">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white" alt="Website logo">
    </a>
</p>

> 🚀 Don't hesitate to follow us on our different networks, and put a star 🌟 on `PoC's` repositories.
