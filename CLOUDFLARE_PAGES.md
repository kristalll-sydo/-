# Cloudflare Pages 部署

这个站点已经按静态网站整理好，推荐直接用 Cloudflare Pages 连接 GitHub 仓库部署。

## 一次性设置

1. 把整个 `Game-Theory-Learning-Repository` 推送到 GitHub。
2. 打开 Cloudflare Dashboard，进入 **Workers & Pages**。
3. 选择 **Create application** -> **Pages** -> **Connect to Git**。
4. 选择这个仓库与要发布的分支。
5. 构建设置：
   - Framework preset: `None`
   - Build command: 留空
   - Build output directory: `.` 或 `/`
   - Root directory: 留空
6. 点击 **Save and Deploy**。

## 访问路径

仓库根目录已经包含：

- `_redirects`：把 `/` 和 `/index.html` 转到 `/site/index.html`
- `_headers`：降低静态资源缓存干扰，方便你继续迭代
- `.nojekyll`：确保中文文件名、PDF、SVG 和资源目录正常发布

部署成功后，Cloudflare 分配的根域名就可以直接打开课程首页。不要把发布目录设成 `site/`，因为讲义、图片、PDF 位于 `site/` 的上级目录，网页依赖这些相对路径访问资源。

## 自定义域名

在 Cloudflare Pages 项目中进入 **Custom domains**，添加你的域名或子域名。若域名也托管在 Cloudflare，DNS 会自动配置；否则按页面提示添加 CNAME。

## 发布前自检

本地先运行：

```powershell
python -m http.server 8765
```

然后打开：

- `http://127.0.0.1:8765/site/index.html`
- `http://127.0.0.1:8765/site/game.html?game=pd`
- 任意一篇讲义阅读页
- 课程 PPT 和 MIT PDF 入口

如果这些本地路径正常，Cloudflare Pages 上也应该正常。
