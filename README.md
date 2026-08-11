# Roumanwu 扩展仓库(Fork)

> **Fork Notice / 分支说明**
>
> 本仓库是 [yuzono/tachiyomi-extensions](https://github.com/yuzono/tachiyomi-extensions)
> 的个人分支(fork),原项目作者为 Yūzōnō,上游扩展仓库位于
> [yuzono/manga-repo](https://github.com/yuzono/manga-repo)。
>
> 我们 fork 这个仓库,是为了单独维护 Roumanwu(肉漫屋)扩展的镜像地址,并搭建一套
> 自己的自动发布流程。除此之外,不对上游代码做任何改动,也不主张任何归属。
> 如果你喜欢这个项目,请支持原作者:
> [GitHub Sponsors](https://github.com/sponsors/cuong-tran)。

## 本分支的改动

- 修正 Roumanwu 镜像地址:默认 `roum28.xyz`(国内可直连),备选 `rouman5.com`。
- 新增自动发布流水线:推送 `master` 后自动构建 APK、生成仓库索引、部署到 GitHub Pages。
- 当前扩展版本:`Roumanwu v1.4.21`。

## 在漫画软件中添加本仓库

Mihon / Komikku → 设置 → 扩展 → 扩展仓库 → 添加仓库,粘贴以下地址:

```
https://9426443.github.io/tachiyomi-extensions/index.pb
```

备用地址(raw):

```
https://raw.githubusercontent.com/9426443/tachiyomi-extensions/gh-pages/index.pb
```

添加后应能看到 `Roumanwu` 扩展,点击安装即可。

## 如何更新扩展

修改 `src/zh/roumanwu/` 下的代码并推送(push)到 `master` 分支,GitHub Actions 会自动
重新构建、更新索引并发布,漫画软件里刷新仓库即可获取新版本。

## 上游与致谢

- 扩展源码仓库:[yuzono/tachiyomi-extensions](https://github.com/yuzono/tachiyomi-extensions)
- 官方扩展仓库(推荐安装,包含全部扩展):[yuzono/manga-repo](https://github.com/yuzono/manga-repo)
- 兼容的阅读应用:[Komikku](https://github.com/komikku-app/komikku)、[Mihon](https://github.com/mihonapp/mihon)

如需请求新源、报告 bug 或参与开发,请优先到上游仓库提交
[Issue](https://github.com/yuzono/tachiyomi-extensions/issues) 或
[Pull Request](https://github.com/yuzono/tachiyomi-extensions/pulls)。

## License

Apache License 2.0。版权归原作者所有,详见 [LICENSE](./LICENSE)。