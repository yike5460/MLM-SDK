# Changelog

## 0.2.0-alpha (2026-05-01)

Full Changelog: [v0.1.0-alpha...v0.2.0-alpha](https://github.com/yike5460/MLM-SDK/compare/v0.1.0-alpha...v0.2.0-alpha)

### Features

* **api:** api update ([e9cffd7](https://github.com/yike5460/MLM-SDK/commit/e9cffd74c15c4bef4667bc5a257ad2bd2d496e30))
* **api:** api update ([029915c](https://github.com/yike5460/MLM-SDK/commit/029915c4121f1930acaac1be3c786aa87f29cdad))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#18](https://github.com/yike5460/MLM-SDK/issues/18)) ([0e87d05](https://github.com/yike5460/MLM-SDK/commit/0e87d05847990a10308dbf3c452380970fcd7254))
* **client:** only call .close() when needed ([#35](https://github.com/yike5460/MLM-SDK/issues/35)) ([5680f4c](https://github.com/yike5460/MLM-SDK/commit/5680f4c4dac2b0330eae4331a5e3e8b758ee48b3))
* correctly handle deserialising `cls` fields ([#38](https://github.com/yike5460/MLM-SDK/issues/38)) ([8ce79b3](https://github.com/yike5460/MLM-SDK/commit/8ce79b3239c9f042a0ed8dd6d0dc428d527663fe))


### Chores

* add missing isclass check ([#33](https://github.com/yike5460/MLM-SDK/issues/33)) ([0b62753](https://github.com/yike5460/MLM-SDK/commit/0b627533b0416866347f252b48af371646207b63))
* **internal:** add support for TypeAliasType ([#24](https://github.com/yike5460/MLM-SDK/issues/24)) ([9d05199](https://github.com/yike5460/MLM-SDK/commit/9d051995bdbc1b31f99d3d2cef8c22f23305ec5a))
* **internal:** bump pydantic dependency ([#21](https://github.com/yike5460/MLM-SDK/issues/21)) ([45900f1](https://github.com/yike5460/MLM-SDK/commit/45900f1edf2936c66bb2cad39f26052011d4dfb4))
* **internal:** bump pyright ([#19](https://github.com/yike5460/MLM-SDK/issues/19)) ([329ccd2](https://github.com/yike5460/MLM-SDK/commit/329ccd26c0211ba87a17ea6394a5da2135f12ee1))
* **internal:** bump pyright ([#23](https://github.com/yike5460/MLM-SDK/issues/23)) ([250e1a0](https://github.com/yike5460/MLM-SDK/commit/250e1a0e7c5feaa837f4a913481b51e4c236f8fa))
* **internal:** codegen related update ([61b10c1](https://github.com/yike5460/MLM-SDK/commit/61b10c1d276f2017b8b5d08211fd4bcd4246fae4))
* **internal:** codegen related update ([6e164c7](https://github.com/yike5460/MLM-SDK/commit/6e164c75bc5673b2b0c1e7adc7311a77cb9bc568))
* **internal:** codegen related update ([4eeb172](https://github.com/yike5460/MLM-SDK/commit/4eeb172e26894ab8fd1afb7b8d5bac20c83791b7))
* **internal:** codegen related update ([94589d1](https://github.com/yike5460/MLM-SDK/commit/94589d10adfe8233f72e8cbbb71003d8d3b0a322))
* **internal:** codegen related update ([e8bd68c](https://github.com/yike5460/MLM-SDK/commit/e8bd68c278b08e95f8272fa975694cec26390dc2))
* **internal:** codegen related update ([df705a8](https://github.com/yike5460/MLM-SDK/commit/df705a81b1f962045de101431b0cd0a3833558c0))
* **internal:** codegen related update ([#16](https://github.com/yike5460/MLM-SDK/issues/16)) ([5786d2d](https://github.com/yike5460/MLM-SDK/commit/5786d2dde180c4f2351515bd4f0f6fa58f96f321))
* **internal:** codegen related update ([#25](https://github.com/yike5460/MLM-SDK/issues/25)) ([35822f6](https://github.com/yike5460/MLM-SDK/commit/35822f6a96eb41ac3e21bf27bd387f294cf009b5))
* **internal:** codegen related update ([#26](https://github.com/yike5460/MLM-SDK/issues/26)) ([0cc8c42](https://github.com/yike5460/MLM-SDK/commit/0cc8c42b7b882ec16509be463d48a2f5eb156d14))
* **internal:** codegen related update ([#28](https://github.com/yike5460/MLM-SDK/issues/28)) ([4d0cc32](https://github.com/yike5460/MLM-SDK/commit/4d0cc3292b649d005155a5905b694e1a8cd1778b))
* **internal:** codegen related update ([#29](https://github.com/yike5460/MLM-SDK/issues/29)) ([0a7603e](https://github.com/yike5460/MLM-SDK/commit/0a7603e8959b483825a64528d814f917f113a87f))
* **internal:** codegen related update ([#32](https://github.com/yike5460/MLM-SDK/issues/32)) ([a0ff9a8](https://github.com/yike5460/MLM-SDK/commit/a0ff9a870f2246ad29f4f368df7f082c7902933a))
* **internal:** codegen related update ([#34](https://github.com/yike5460/MLM-SDK/issues/34)) ([77413c9](https://github.com/yike5460/MLM-SDK/commit/77413c993bbf2e217f733415ca3cc8ee5b9a2e09))
* **internal:** codegen related update ([#37](https://github.com/yike5460/MLM-SDK/issues/37)) ([6a409d9](https://github.com/yike5460/MLM-SDK/commit/6a409d964297ff2a9af4955463e1891a713de229))
* **internal:** codegen related update ([#39](https://github.com/yike5460/MLM-SDK/issues/39)) ([a819b06](https://github.com/yike5460/MLM-SDK/commit/a819b06b50d8babf46debea7b2f92e179210dd16))
* **internal:** exclude mypy from running on tests ([#17](https://github.com/yike5460/MLM-SDK/issues/17)) ([d8982ad](https://github.com/yike5460/MLM-SDK/commit/d8982adb1d4efd7633c68000bc712d4c27c3b98b))
* **internal:** fix compat model_dump method when warnings are passed ([#14](https://github.com/yike5460/MLM-SDK/issues/14)) ([204354c](https://github.com/yike5460/MLM-SDK/commit/204354cc2fbdcc1ea65f859b4a35a33060cbffe6))
* **internal:** fix some typos ([#31](https://github.com/yike5460/MLM-SDK/issues/31)) ([72d3612](https://github.com/yike5460/MLM-SDK/commit/72d3612bb977f2e514db06fdecc90f3b8504a63d))
* **internal:** updated imports ([#27](https://github.com/yike5460/MLM-SDK/issues/27)) ([c0e4905](https://github.com/yike5460/MLM-SDK/commit/c0e49050a9e4bc82b9d97b4cb4f5ecbe693e9219))
* make the `Omit` type public ([#20](https://github.com/yike5460/MLM-SDK/issues/20)) ([74ea7b5](https://github.com/yike5460/MLM-SDK/commit/74ea7b5bd96ec6f2a80e7e5398c41b114cb5bcef))
* rebuild project due to codegen change ([#10](https://github.com/yike5460/MLM-SDK/issues/10)) ([9e01178](https://github.com/yike5460/MLM-SDK/commit/9e01178678a65e7c99fd9d1077975ed0421911af))
* rebuild project due to codegen change ([#12](https://github.com/yike5460/MLM-SDK/issues/12)) ([359ea0d](https://github.com/yike5460/MLM-SDK/commit/359ea0d1a864eea390376a48cc3e30a50cd000d4))
* rebuild project due to codegen change ([#13](https://github.com/yike5460/MLM-SDK/issues/13)) ([1840691](https://github.com/yike5460/MLM-SDK/commit/1840691a41ac0ebe958179433caf239f9de3c853))
* **tests:** bump steady to v0.20.2 ([ad71ee4](https://github.com/yike5460/MLM-SDK/commit/ad71ee448072fbe0b47bacd1ef2752a796a60059))


### Documentation

* add info log level to readme ([#15](https://github.com/yike5460/MLM-SDK/issues/15)) ([90b10ab](https://github.com/yike5460/MLM-SDK/commit/90b10ab3ff10020f3848413e51316947f4909033))
* fix typos ([#36](https://github.com/yike5460/MLM-SDK/issues/36)) ([7bc62b2](https://github.com/yike5460/MLM-SDK/commit/7bc62b2ce6384088c200bf9ef33f864671f3ad8f))
* **readme:** example snippet for client context manager ([#30](https://github.com/yike5460/MLM-SDK/issues/30)) ([a4aec1c](https://github.com/yike5460/MLM-SDK/commit/a4aec1c6c90949db568be7880e5fc08b1d3bdece))
* **readme:** fix http client proxies example ([#22](https://github.com/yike5460/MLM-SDK/issues/22)) ([1cfce26](https://github.com/yike5460/MLM-SDK/commit/1cfce26f6a921f4ace11ebf3709705a75c225f64))

## 0.1.0-alpha (2024-05-17)

Full Changelog: [v0.0.2-alpha...v0.1.0-alpha](https://github.com/yike5460/MLM-SDK/compare/v0.0.2-alpha...v0.1.0-alpha)

### Features

* docs: update openapi spec ([a1ded77](https://github.com/yike5460/MLM-SDK/commit/a1ded779422fd9ce0279342b34b050fc0d52d1e4))


### Documentation

* Update ci.yml ([222a378](https://github.com/yike5460/MLM-SDK/commit/222a378cd12a262e9744c9dff9c192dfad6bc043))

## 0.0.2-alpha (2024-05-17)

Full Changelog: [v0.0.1-alpha...v0.0.2-alpha](https://github.com/yike5460/MLM-SDK/compare/v0.0.1-alpha...v0.0.2-alpha)

### Chores

* update SDK settings ([#5](https://github.com/yike5460/MLM-SDK/issues/5)) ([44f3e04](https://github.com/yike5460/MLM-SDK/commit/44f3e04f6d3d891b63366310fea0d8ae6cd7a07d))

## 0.0.1-alpha (2024-05-17)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha](https://github.com/yike5460/MLM-SDK/compare/v0.0.1-alpha.0...v0.0.1-alpha)

### Chores

* go live ([#1](https://github.com/yike5460/MLM-SDK/issues/1)) ([87205bc](https://github.com/yike5460/MLM-SDK/commit/87205bcfd4128639ee8e29898403aa50482fb78e))
* update SDK settings ([#3](https://github.com/yike5460/MLM-SDK/issues/3)) ([28d4722](https://github.com/yike5460/MLM-SDK/commit/28d47229dc3eb66462c7f5a0c5d1424ea334b8e6))
