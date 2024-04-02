# XV3DGS-AirSim
搭建一个在Real2Sim模式中开飞机/汽车的workflow
## 使用
我们需要使用UE5.2 + Windows，结合[官方教程](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#plugin-download)，在官方release界面下载5.2版本的插件，并解压放置在`Plugins`文件夹内，然后启动projects即可，接下来我们不需要默认使用官方提供的[windows本地训练3DGS脚本](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#local-training-on-windows-platform)，而也可以使用我们自己的方法，只要最终得到ply点云文件，即可用[XV3DGS插件](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#import-your-guassian-splatting-model)轻松导入到UE Editror中进行使用，并且适用官方提供的[种种特性](https://github.com/xverse-engine/XV3DGS-UEPlugin?tab=readme-ov-file#feature-introduction)（如仿射变换、裁剪、打光、变色）,这里不做赘述。