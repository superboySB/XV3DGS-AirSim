# XV3DGS-AirSim
搭建一个在Real2Sim模式中开飞机/汽车的workflow

## 依赖
- 良好的拍摄一段视频（示例）
- XV3DGS虚幻插件


## 使用
**我们需要使用UE5.2 + Windows**，结合[官方教程](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#plugin-download)，在官方release界面下载5.2版本的插件，并解压放置在`Plugins`文件夹内，然后启动projects即可，接下来我们不需要默认使用官方提供的[windows本地训练3DGS脚本](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#local-training-on-windows-platform)，而也可以使用我们自己的方法，只要注意官方说的[事项](https://github.com/xverse-engine/XV3DGS-UEPlugin/blob/main/Media/CaptureDOC_CN.md)合理拍摄一个mp4，最终就能训练得到一个还可以的相应ply点云文件，并用[XV3DGS插件](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#import-your-guassian-splatting-model)轻松导入到UE Editror中进行使用，这里官方还提供了[种种特性](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#feature-introduction)（如仿射变换、裁剪、打光、变色）,这里不做赘述。具体Airsim的用法参考知乎大佬：宁子安。



[![9204209a036a4cc5118a55819e81a50.png](https://i.postimg.cc/pyMNxC7M/9204209a036a4cc5118a55819e81a50.png)](https://postimg.cc/YLRDz6Md)

[![9d2bf9c51bf73069ae41e836ef430aa.png](https://i.postimg.cc/QC2DChFP/9d2bf9c51bf73069ae41e836ef430aa.png)](https://postimg.cc/RJLybrQQ)

