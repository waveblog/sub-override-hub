## 使用说明

- 个人修改 mihomo 覆写配置，只在 sub-store 中测试覆写成功， mihomo-party/sparkle 请自行测试

- 正常用户请使用 [selfuse_dns.yaml](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/selfuse_dns.yaml) 配置， [selfuse_dns_local.yaml](https://raw.githubusercontent.com/Seameee/override-hub/refs/heads/main/selfuse_dns_local.yaml) 为本地 DNS 分流用户配置文件，DNS模式使用 redir-host，需自行修改为已经做好 DNS 分流的 AdGuardHome DNS / MosDNS 地址

- 新增一个 sub-store 的组合订阅模板。因覆写中代理组的正则表达式可能存在测试不完整的情况，所以建议使用我的组合订阅模板，内置功能包括节点重命名、节点排序、去除风险节点、替换旗帜、IPv6 入口解析（可自行开启）、组合订阅获取多机场流量信息、家宽 / 落地节点自动设置代理链


---------------------------

**以下为致谢内容，排序不分先后**

- [mihomo-party-org/override-hub](https://github.com/mihomo-party-org/override-hub)
- [Keywos/rule](https://github.com/Keywos/Rule)
- https://linux.do/t/topic/496229
- https://t.me/zhetengsha/2197