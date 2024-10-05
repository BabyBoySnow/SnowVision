[release-badge]: https://img.shields.io/github/v/release/BabyBoySnow/SnowVision?include_prereleases&style=flat-square
[release-link]: https://github.com/BabyBoySnow/SnowVision/releases
[license-badge]: https://img.shields.io/github/license/BabyBoySnow/SnowVision?style=flat-square
[license-link]: https://github.com/BabyBoySnow/SnowVision/blob/master/LICENSE
[discord-badge]: https://discord.com/api/guilds/212324635356692500/widget.png?style=shield
[discord-link]: https://clearvision.github.io/join
[issues-badge]: https://img.shields.io/github/issues/BabyBoySnow/SnowVision?style=flat-square
[issues-link]: https://github.com/BabyBoySnow/SnowVision/issues
[prs-badge]: https://img.shields.io/github/issues-pr/BabyBoySnow/SnowVision?style=flat-square
[prs-link]: https://github.com/BabyBoySnow/SnowVision/pulls

<div align="center">

# ClearVision v6 (SnowVision Fork)

[![Releases][release-badge]][release-link]
[![License][license-badge]][license-link]
[![Discord Server][discord-badge]][discord-link]
[![Issues][issues-badge]][issues-link]
[![Pull Requests][prs-badge]][prs-link]

![Winter Wonderland Preview](https://i.imgur.com/6gKOP6i.png)

</div>

## Installation

### Winter Wonderland

1. Download the [Winter Wonderland CSS file](https://github.com/BabyBoySnow/SnowVision/blob/master/Winter%20Wonderland.css).
2. Move it to your theme folder.
3. This theme uses the Amazon Kindle font ["Bookerly"](https://www.cufonfonts.com/font/bookerly) and a custom font ["Lovely Home"](https://www.dafont.com/lovely-home.font).

### SnowVision

**Note:** This fork of ClearVision doesn't actively support plugins but tries to maintain compatibility with widely used ones.

#### For BetterDiscord and Vencord:

1. Download the theme file from [Releases](https://github.com/BabyBoySnow/SnowVision/releases).
2. Move the file into your injector's themes folder:
   - **BetterDiscord:** `%appdata%\betterdiscord\themes`
   - **Vencord:** `%appdata%\vencord\themes`

### For Replugged (Coming Soon)

Support for Replugged is currently in development. Stay tuned for updates!

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
- Moved the new message pill to the middle.
- Removed some borders and added more shading.
- Removed glow from the wordmark. Changed to "Winter Wonderland v1.3.2".
- Used snippet from [NyxIsBad](https://github.com/NyxIsBad) to make non-Nitro users look cool.
- Applied snippet to fit long plugin names inside the box.
- Enhanced pings to stand out more.
- Changed the border on the Spotify controls plugin for Vencord.
- Rounded a few buttons.
- Darkened Vencord plugin boxes.
- Changed Vencord plugin info text color to white (`#fff`).
- Changed the status on the profile pop outs. Further adjustment needed.
- Various other changes and improvements.
