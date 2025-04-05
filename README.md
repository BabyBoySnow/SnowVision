
# Aquarion: Immerse Yourself in a Smoother ClearVision Experience

[prettier-badge]: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square  
[prettier-link]: https://github.com/prettier/prettier  
[sass-badge]: https://img.shields.io/badge/Sass-CC6699.svg?style=flat-square&logo=sass&logoColor=white  
[sass-link]: https://sass-lang.com/  
[release-badge]: https://img.shields.io/github/v/release/Aquarion-D/Aquarion?include_prereleases&style=flat-square  
[release-link]: https://github.com/Aquarion-D/Aquarion/releases  
[license-badge]: https://img.shields.io/github/license/Aquarion-D/Aquarion?style=flat-square  
[license-link]: https://github.com/Aquarion-D/Aquarion/blob/Aquarion/LICENSE  
[issues-badge]: https://img.shields.io/github/issues/Aquarion-D/Aquarion?style=flat-square  
[issues-link]: https://github.com/Aquarion-D/Aquarion/issues  
[prs-badge]: https://img.shields.io/github/issues-pr/Aquarion-D/Aquarion?style=flat-square  
[prs-link]: https://github.com/Aquarion-D/Aquarion/pulls  

<div align="center">

[![code style: prettier][prettier-badge]][prettier-link]  
[![Language: Sass][sass-badge]][sass-link]  
[![Releases][release-badge]][release-link]  
[![License][license-badge]][license-link]  
[![Issues][issues-badge]][issues-link]  
[![Pull Requests][prs-badge]][prs-link]  

![Main Aquarion Preview](https://raw.githubusercontent.com/Aquarion-D/Aquarion/refs/heads/Aquarion/screenshots/Aquarion%20Preview.png)

<details>
  <summary>Click to view additional previews</summary>

   ![Nitro Profile Preview](https://github.com/Aquarion-D/Aquarion/raw/Aquarion/screenshots/Nitro%20Profile%20Preview.png)  
   ![Regular Profile](https://github.com/Aquarion-D/Aquarion/raw/Aquarion/screenshots/Preview%20with%20profile.png)
   ![Channel Hovered](https://raw.githubusercontent.com/Aquarion-D/Aquarion/refs/heads/Aquarion/screenshots/Channel%20Hovered.png)

</details>

</div>

## Credit

Huge thanks to [NyxIsBad](https://github.com/NyxIsBad) for helping me get this up and running!

The **Aquarion Logo** is available for free download [here](https://www.kindpng.com/imgv/hwbRbbo_emoji-snow-snowflake-holographic-snowflake-emoji-png-transparent/).

[Sessh](<https://discord.com/users/294957734552535040>) on discord, has helped by finding bugs and things that needed adjusted.

## Installation

### **Aquarion Theme**

1. Download the [Aquarion CSS file](https://raw.githubusercontent.com/Aquarion-D/Aquarion/Aquarion/Aquarion.theme.css).
2. Move it to your theme folder.
   - On **Windows**, press `Win + R`, type `%appdata%`, then navigate to your Discord client's `themes` folder.

This theme features:
   - **["Bookerly"](https://www.cufonfonts.com/font/bookerly)** (Amazon Kindle font) for better readability.
   - **["Lovely Home"](https://www.dafont.com/lovely-home.font)** for branding, giving the "Aquarion" watermark a unique, stylish look.

### **For BetterDiscord and Vencord:**

1. Download the theme file from [Releases](https://github.com/Aquarion-D/Aquarion/releases).
2. Move it into your injector's theme folder:
   - **BetterDiscord:** `%appdata%Betterdiscord	hemes`
   - **Vencord:** `%appdata%Vencord	hemes`

### **For Replugged:**

1. Download the [Aquarion CSS file](https://raw.githubusercontent.com/Aquarion-D/Aquarion/Aquarion/Aquarion.theme.css).
2. (Optional) Customize it to your liking.
3. Convert it using [Replugged’s theme converter](https://replugged-org.github.io/theme-converter/).
4. Open **Settings** → **Themes** → Install the converted file.

Alternatively, you can copy the CSS into **Custom CSS**.

**Note:** This fork of ClearVision doesn’t actively support plugins but tries to maintain compatibility with widely used ones.

### **Customization**

If you're using **BetterDiscord**, you can edit the theme directly in settings.  
For **Vencord**, follow these steps:

1. Open **User Settings** → **Themes** → Click **"Open themes folder"**
2. Open `aquarion.theme.css` and edit the CSS variables.
   - Example: To change the background, modify `--background-image` with a new image URL.
   - **Note:** The URL must use **HTTPS** and end in an image format (e.g., `.png`, `.jpeg`).

## Building from Source

To build the theme from source:

1. Install **Node.js/npm** ([Download here](https://nodejs.org/)).
2. Run the following commands:

```sh
npm install  # Install dependencies
npm run build  # Compile the theme (output in /public)
npm run test  # Compile test output in /test (for manual previewing)
```

3. To test changes before pushing:

```sh
npm run test # Outputs a 'main.css' file in /test
```

4. Move `main.css` to your theme folder and enable it in your client.

### Dependencies

- [NodeJS/npm](https://nodejs.org/)
- [sass](https://www.npmjs.com/package/sass)
- [PostCSS Autoprefixer](https://www.npmjs.com/package/autoprefixer)
- [PostCSS CLI](https://www.npmjs.com/package/postcss-cli)
- [rimraf](https://www.npmjs.com/package/rimraf) (for cleanup)
- [Prettier](https://www.npmjs.com/package/prettier) (code formatting)

## Contributing

1. Clone the repository.
2. Run `npm run test` to generate `main.css` in the `/test` directory.
3. Copy `main.css` into BetterDiscord’s Custom CSS or your theme folder.
4. Disable other themes while testing for best results.

---

 <details>
  <summary>Changelog</summary>

- Moved date dividers to the middle.
- Added new options for `alt-color` to use in several places.
- Removed the annoying help message from HepBoat in the ClearVision Support server.
- Removed the border around Nitro for "most popular."
- Added radical status.
- Changed activity texts to use the alt-color.
- Moved the new message pill to the middle, removed the dividers, made it alt color, and made it square.
- Changed the server member's list to use alt color for roles and the lines on the side to be main color.
- Changed server channel category names to use alt color.
- Removed some borders and added more shading.
- Removed glow from the wordmark. Changed to "Aquarion v1.5.5".
- Theme button whites to main color.
- Made text box use background-shading.
- Changed the border on the Spotify controls plugin for Vencord.
- Rounded a few buttons.
- Darkened Vencord plugin boxes.
- Changed Vencord plugin info text color to white (`#fff`).
- Removed the bubbles for statuses, as well as tried to make most of them transparent with the main color as a border.
- Changed the guild folders to be slightly transparent versions of the main color.
- Slightly darkened the voice count.
- Added support for the Vencord plugin to send voice messages.
- Background of the home icon made to be transparent so that if the image doesn't fill it all, it doesn't look weird.
- Removed the home shop mosaic.
- In settings, under nitro, changed the button shine to alt color and slowed it down a little.
- Changed the message request section to use the same style as hovering over a regular message, makes it a little easier to see.
- Changed the tags some for credit to myself.
- Edited the keybind recording in settings for voice and video push-to-talk to make it easier to see while recording.
- Removed the background of the Discord shop so that you can see the custom background.
- Made it easier to see the last played time for games.
- Weird pop-up about "looking for blocked users?" has been made transparent.
- Made the forums list title slightly less intrusive. No one likes a flashbang.
- Also changed the forums user and message content to be easier to see.
- Added hover effect to emoji remove in server settings.
- In user settings -> boost, adjusted popup about boost having a new home to be slightly transparent, also padded the "boost not used" popout.
- Applied background overlay to the boost mural in server menu -> boost this server.
- Changed the button to use white.
- Adjusted the forums start chat to be easier to see.
- Added an option to enable a frosted glass effect.
- A lot more stuff that I can't be bothered to type. For a complete history of changes, it's best to read the [commits](https://github.com/Aquarion-D/Aquarion/commits/Aquarion/).

</details>