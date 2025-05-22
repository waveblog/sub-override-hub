# 自修改 override-hub 项目说明

自修改的 mihomo 覆写配置和 sub-store 组合订阅模板

## 使用指南

### mihomo 配置
- 本配置已在 sub-store 中测试通过，mihomo-party/sparkle 请自行测试
- 配置文件：
  - [selfuse_dns.yaml](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/selfuse_dns.yaml) - 普通用户使用
  - [selfuse_dns_local.yaml](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/selfuse_dns_local.yaml) - 本地 DNS 分流用户使用
    - 仅修改 DNS 部分为 redir-host，其他都和 [selfuse_dns.yaml](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/selfuse_dns.yaml) 同步
    - 需自行修改为已配置 DNS 分流的 AdGuardHome DNS / MosDNS 地址
  - [selfuse_test_remote.yaml](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/selfuse_test_remote.yaml) 和 [selfuse_test_local.yaml](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/selfuse_test_local.yaml)为测试配置，请自行选用

### sub-store 懒人配置
预置了 sub-store 的懒人配置，导入后添加你的订阅就能使用
1. 组合订阅模板
   - 功能包括：
     - 节点重命名
     - 节点排序
     - 去除风险节点
     - 替换旗帜
     - IPv6 入口解析（可选）
     - 多机场流量信息整合
     - 家宽/落地节点自动设置代理链
   - 使用方法：
     - 在 sub-store 订阅管理页面，点击左上角 ➕ 号
     - 将 [sub-store组合订阅模板](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/sub-store组合订阅模板.json) 导入本地配置
     - 选择需要整合的机场订阅并保存

2. 托管配置模板
   - 使用方法：
     - 在 sub-store 文件管理页面，点击左上角 ➕ 号
     - 将 [mihomo配置](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/mihomo配置.json) 导入本地配置
     - 选择上一步生成的组合订阅并保存

## 致谢
特别感谢以下项目和个人（排名不分先后）：
- [mihomo-party-org/override-hub](https://github.com/mihomo-party-org/override-hub)
- [Keywos/rule](https://github.com/Keywos/Rule)
- https://linux.do/t/topic/496229
- https://t.me/zhetengsha/2197
- [cmliu/ACL4SSR](https://github.com/cmliu/ACL4SSR)
