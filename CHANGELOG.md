# Changelog

## 0.1.0-alpha.1 (2025-02-28)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/ChristopheDujarric/test-train-travel-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **client:** allow passing `NotGiven` for body ([#18](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/18)) ([6da8c8e](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/6da8c8eb3c1efbe2b04eddfa9a879a59fa1c82e2))
* **client:** send `X-Stainless-Read-Timeout` header ([#10](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/10)) ([c233c9a](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/c233c9a257ac955e7c28531f0b86936df2ac5898))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#16](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/16)) ([6c62e11](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/6c62e11df9fa6ba71f7bec6d58cf9bbf2080d6d9))
* **client:** mark some request bodies as optional ([6da8c8e](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/6da8c8eb3c1efbe2b04eddfa9a879a59fa1c82e2))
* deduplicate unknown entries in union ([#7](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/7)) ([ef995a5](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/ef995a5ec620eeb454e1e82ad83c1fd23c86645b))
* **tests:** correctly generate examples with writeOnly fields ([#6](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/6)) ([e6a4ff3](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/e6a4ff3817b778ab6956f99a04e3d1b8838bb54b))


### Chores

* **docs:** update client docstring ([#22](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/22)) ([6f01422](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/6f014226a9514d4131088a82d029d7724efb81b9))
* go live ([#1](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/1)) ([b9687a1](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/b9687a129c84980ac67f37229503fd1e26f14f98))
* **internal:** bummp ruff dependency ([#9](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/9)) ([d0715da](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/d0715da982bac7855d59a40c98ca7add457f0304))
* **internal:** change default timeout to an int ([#8](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/8)) ([3116634](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/31166348eb0b484dfa69ec379ad4b85da876078a))
* **internal:** codegen related update ([#4](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/4)) ([1a95a89](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/1a95a8960b6d37997b64385b73a012634744c997))
* **internal:** fix devcontainers setup ([#19](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/19)) ([c6181a7](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/c6181a7bef906593f947270dd88e2c0310e8c9b6))
* **internal:** fix type traversing dictionary params ([#11](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/11)) ([59c4027](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/59c4027f9afa5991558a22aa251d3ffea8a5c6e4))
* **internal:** minor formatting changes ([#5](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/5)) ([58f1d0e](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/58f1d0eb519cec3fcd9dbfb58cb401c2d1a2a10e))
* **internal:** minor type handling changes ([#12](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/12)) ([a3a4b07](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/a3a4b079fc5358f66ed3cfa218fdc8a750180859))
* **internal:** properly set __pydantic_private__ ([#20](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/20)) ([6644ee3](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/6644ee38b3b264b3c9e2f40694c5dd7857688a47))
* **internal:** update client tests ([#15](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/15)) ([f105253](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/f105253f3cd82443f6649d3f1ea34c0fbdfac114))
* **internal:** update client tests ([#17](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/17)) ([80e9c36](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/80e9c365b68248b6f4e2c052588cd2d1717a88e4))
* minor change to tests ([#13](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/13)) ([6555cb7](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/6555cb75d80895f854d353a489e4722cc5bd4694))
* update SDK settings ([#3](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/3)) ([e3937e1](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/e3937e1f7c12970c6ec2e7cec3ef11bde092c173))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#21](https://github.com/ChristopheDujarric/test-train-travel-sdk/issues/21)) ([125ce27](https://github.com/ChristopheDujarric/test-train-travel-sdk/commit/125ce27ae56552a258369ab7f217f8c5fea6dea8))
