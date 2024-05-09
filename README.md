[release-badge]: https://img.shields.io/github/v/release/ClearVision/ClearVision-v6?include_prereleases&style=flat-square
[release-link]: https://github.com/ClearVision/ClearVision-v6/releases
[license-badge]: https://img.shields.io/github/license/ClearVision/ClearVision-v6?style=flat-square
[license-link]: https://github.com/ClearVision/ClearVision-v6/blob/master/LICENSE
[discord-badge]: https://discord.com/api/guilds/212324635356692500/widget.png?style=shield
[discord-link]: https://clearvision.github.io/join
[issues-badge]: https://img.shields.io/github/issues/ClearVision/ClearVision-v6?style=flat-square
[issues-link]: https://github.com/ClearVision/ClearVision-v6/issues
[prs-badge]: https://img.shields.io/github/issues-pr/ClearVision/ClearVision-v6?style=flat-square
[prs-link]: https://github.com/ClearVision/ClearVision-v6/pulls

<div align="center">

# ClearVision v6

[![Releases][release-badge]][release-link]
[![License][license-badge]][license-link]
[![Discord Server][discord-badge]][discord-link]
[![Issues][issues-badge]][issues-link]
[![Pull Requests][prs-badge]][prs-link]

![v1](https://i.imgur.com/p99DoDp.png)

</div>

## Installing Winter Wonderland

Follow the instructions above for injectors except replugged. Download the [file](https://github.com/BabyBoySnow/SnowVision/blob/master/Winter%20Wonderland.css) and move it to your theme folder. This theme uses the Amazon kindle font ["Bookerly"](https://www.cufonfonts.com/font/bookerly) and a custom font ["lovely home"](https://www.dafont.com/lovely-home.font)

## Installing official ClearVision

Note: ClearVision doesn't actively support plugins (as in, we don't seek out and actively theme fixes to every new plugin). However, when a plugin is widely used, we try our best to stay compatible.

**For BD and Vencord:**

Download the theme file from [our official support server](https://clearvision.github.io/join), [the BetterDiscord Website](https://betterdiscord.app/theme/ClearVision) or [releases](https://github.com/ClearVision/ClearVision-v6/releases) and move it into your injector's themes folder:

- BetterDiscord: `%appdata%\betterdiscord\themes`
- Vencord: `%appdata%\vencord\themes`

**For Replugged:**

Check out our replugged theme [here!](https://github.com/ClearVision/CV-Replugged)

## Theme Editor

You can now customize the theme with a preview before downloading it to your computer.

Please keep in mind that **we do not manage the theme editor**, and cannot help with any bugs that come from using it.

> [Theme Editor](https://bdeditor.dev/theme/clearvision)

_Thank you to @Gibbu to providing this._

## Building from source

To build the theme from source, you can simply run `npm install` to install all missing dependencies and `npm run build` to compile the theme into the `/public` folder.

### Dependencies

- [NodeJS/npm](https://nodejs.org/)
- [sass](https://www.npmjs.com/package/sass)
- [PostCSS Autoprefixer](https://www.npmjs.com/package/autoprefixer)
- [PostCSS CLI](https://www.npmjs.com/package/postcss-cli)
- [rimraf](https://www.npmjs.com/package/rimraf) (for cleanup)
- [Prettier](https://www.npmjs.com/package/prettier) (code formatting)

## Contributing

You can run `npm run test` to compile the theme.
The `main.css` file will be in the `/test` directory, which can then be copied into BetterDiscord's Custom CSS.

## Changelog

- Move date dividers to the middle.
- add new options alt-color to use in several places.
- Remove the annoying help message from hepboat in ClearVision Support server
- Remove annoying border around nitro for "most popular".
- Use radical status.
- Move new message pill to the middle.
- Remove some borders on stuff, use more shading.
- Remove glow from wordmark. Change to "Winter Wonderland v1.3.2".
- Use snippet from [NyxIsBad](https://github.com/NyxIsBad) to make non nitro users look cool.
- Use snippet from [NyxIsBad](https://github.com/NyxIsBad) to fit long plugin names inside the box.
- Use snippet to make pings stand out more and look cool.
- Changes the border on the spotify controls plugin for vencord.
- Make a few buttons round.
- Darken vencord plugin boxes
- Color vencord plugin info to #fff(white)
- Various changes and improvements, information not provided by developer.
