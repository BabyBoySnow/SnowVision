[prettier-badge]: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square
[prettier-link]: https://github.com/prettier/prettier
[sass-badge]: https://img.shields.io/badge/Sass-CC6699.svg?style=flat-square&logo=sass&logoColor=white
[sass-link]: https://sass-lang.com/
[release-badge]: https://img.shields.io/github/v/release/BabyBoySnow/SnowVision?include_prereleases&style=flat-square
[release-link]: https://github.com/BabyBoySnow/SnowVision/releases
[license-badge]: https://img.shields.io/github/license/BabyBoySnow/SnowVision?style=flat-square
[license-link]: https://github.com/BabyBoySnow/SnowVision/blob/master/LICENSE
[issues-badge]: https://img.shields.io/github/issues/BabyBoySnow/SnowVision?style=flat-square
[issues-link]: https://github.com/BabyBoySnow/SnowVision/issues
[prs-badge]: https://img.shields.io/github/issues-pr/BabyBoySnow/SnowVision?style=flat-square
[prs-link]: https://github.com/BabyBoySnow/SnowVision/pulls

<div align="center">

# SnowVision (ClearVision v6 fork)

[![code style: prettier][prettier-badge]][prettier-link]
[![Language: Sass][sass-badge]][sass-link]
[![Releases][release-badge]][release-link]
[![License][license-badge]][license-link]
[![Issues][issues-badge]][issues-link]
[![Pull Requests][prs-badge]][prs-link]

![Winter Wonderland Preview](https://i.imgur.com/UthprMK.png)

</div>

## Credit

Huge thanks to [NyxIsBad](https://github.com/NyxIsBad) for helping me get this up and running!

## Installation

### Winter Wonderland

1. Download the [SnowVision CSS file](https://raw.githubusercontent.com/BabyBoySnow/SnowVision/refs/heads/master/SnowVision.theme.css).
2. Move it to your theme folder, for windows you can type `%appdata%` in the search, and find your client, it should have a theme folder.
3. This theme uses the Amazon Kindle font ["Bookerly"](https://www.cufonfonts.com/font/bookerly) and a custom font ["Lovely Home"](https://www.dafont.com/lovely-home.font).

### SnowVision

**Note:** This fork of ClearVision doesn't actively support plugins but tries to maintain compatibility with widely used ones.

#### For BetterDiscord and Vencord:

1. Download the theme file from [Releases](https://github.com/BabyBoySnow/SnowVision/releases).
2. Move the file into your injector's themes folder:
   - **BetterDiscord:** `%appdata%\betterdiscord\themes`
   - **Vencord:** `%appdata%\vencord\themes`

### For Replugged

1. Download the theme from [SnowVision CSS file](https://raw.githubusercontent.com/BabyBoySnow/SnowVision/refs/heads/master/SnowVision.theme.css)
2. (Optional) Customize it to your hearts content.
3. Convert it using https://replugged-org.github.io/theme-converter/
4. Go into settings, find "themes" and install it in there somewhere.

Alternatively throw everything into custom CSS.

## Building from source

To build the theme from source, first install npm from the dependecies below, then you can run `npm install` to install all missing dependencies and `npm run build` to compile the theme into the `/public` folder.

### Dependencies

- [NodeJS/npm](https://nodejs.org/)
- [sass](https://www.npmjs.com/package/sass)
- [PostCSS Autoprefixer](https://www.npmjs.com/package/autoprefixer)
- [PostCSS CLI](https://www.npmjs.com/package/postcss-cli)
- [rimraf](https://www.npmjs.com/package/rimraf) (for cleanup)
- [Prettier](https://www.npmjs.com/package/prettier) (code formatting)

## Contributing

You can run `npm run test` to compile the theme.
The `main.css` file will be in the `/test` directory, which can then be copied into BetterDiscord's Custom CSS, or placed in the themes folder and enabled in settings, make sure any other theme's are disabled for testing.

## Changelog

### SnowVision (Differences from Original ClearVision)

- Moved date dividers to the middle.
- Added new options for `alt-color` to use in several places.
- Removed the annoying help message from HepBoat in the ClearVision Support server.
- Removed the border around Nitro for "most popular."
- Added radical status.
- Change activety text's to use the alt-color.
- Moved the new message pill to the middle, remove the dividers, made it alt color, and made it square.
- Changed the server member's list to use alt color for roles and the lines on the side to be main color.
- Changed server channel catagory names to use alt color.
- Removed some borders and added more shading.
- Removed glow from the wordmark. Changed to "SnowVision v1.5.5".
- Theme button white's to main color.
- Make text box use background-shading.
- Changed the border on the Spotify controls plugin for Vencord.
- Rounded a few buttons.
- Darkened Vencord plugin boxes.
- Changed Vencord plugin info text color to white (`#fff`).
- Removed the bubbles for statuses, as well as try to make most of them transparent with the main color as a border.
- Change the guild folders to be slightly transparent version of main color.
- Slightly darken the voice count.
- Support for vencord plugin to send voice messages.
- Background of the home icon made to be transparent so that if the image doesn't fill it all it doesn't look weird.
- Removed the home shop mosiac.
- In settings, under nitro, changed the button shine to alt color and slowed it down a little.
- Changed the message request section to use the same style as hovering over a regular message, makes it a little easier to see.
- C hange the tags some for credit to myself.
- Edit the keybind recording in settings for voice and video push to talk to make it easier to see while recording.
- Remove the background of the discord shop so that you can see the custom background.
- Make it easier to see the last played time for games.
- Weird pop up about "looking for blocked users?" has been made transparent.
- Make forums list title slightly less intrusive. No-one likes a flashbang.
- Also change the forums user and message content to be easier to see.
- Add hover effect to emoji remove in server settings.
- In user settings -> boost, adjust popup about boost having a new home to be slightly transparent, also pad the "boost not used" thing.
- Color the message reply spine thing.
- Apply background overlay to boost mural in server menu -> boost this server.
- Change the button to use white.
- Adjust the forums start chat to be easier to see.
- A lot more stuff that I can't be bothered to type. For a complete history of changes, it's best to read the [commits](https://github.com/BabyBoySnow/SnowVision/commits/master/)

---

## Addons

Any changes I make that I feel should not be in the main theme will be included in the [Addons](https://github.com/BabyBoySnow/SnowVision/tree/master/Addons) folder.
To use one you can just take the css file and load it seperately as a theme, or copy the contents into your custom css. Currently includes:

- a change to the behavior of the vencord read all plugin.
- a change to code blocks which requires the custom font [Fira Code.](https://github.com/tonsky/FiraCode/releases)
- a change to the message box to have a breathing effect.

## Scripts

Any scripts I make to aid will be included. Currently includes:

- the file I use to automatically detect if there is any versions of variables that can be converted into
  shorthands. Shorthands are located [here.](https://github.com/BabyBoySnow/SnowVision/blob/master/src/variables.scss)
- a file to update raw css with the [placeholders.](https://github.com/BabyBoySnow/SnowVision/blob/master/lib/selectors/selectorPlaceholders.scss)
- a file that tries to remove any placeholders that don't exist.
