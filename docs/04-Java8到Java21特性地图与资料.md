# Java 8 到 Java 21：特性地图与教师核对资料

> 资料核对：2026-10-12；教学时机按基础优先 v0.2 调整。第一周不要求新语法；先通过输入、方法、对象、集合的个人练习，再按需要短对比。只选课堂会用到的内容，不按版本完整讲 JEP。项目默认不启用预览。

## 1. 先告诉学生的三个区别

- “使用 JDK 21”不意味着每段代码都要采用新语法，也不意味着 Java 8 学过的代码全部失效。
- “Java 8 之后新增、Java 21 可用”和“Java 21 才正式加入”要分开讲。
- 校内作业与拓展项目可以用不同 JDK/语言级别；不要为了拓展课破坏学校原有配置。先记录校内环境，再给拓展项目单独配置 JDK 21。

## 2. 建议教学地图

| 内容 | 正式版本/性质 | 课堂安排 | 学生需要达到的程度 |
|---|---|---|---|
| 类、接口、集合、泛型、异常 | Java 8 已具备 | 第 1–6 周逐步学习并验证 | 独立用，不作为 Java 21 新特性 |
| Lambda、Stream | Java 8 已具备 | 基础整合关卡通过后，搜索/统计选做 | 能把简单 Stream 改回循环；不强制所有循环改 Stream |
| List.of / Set.of / Map.of | Java 9 集合工厂方法 | 集合基本任务通过后短对比 | 返回不可修改集合；发布商品需要可变集合，不直接对 List.of 的结果 add [S9] |
| var | Java 10，本地变量类型推断 | 第 3–6 周基础达标后选讲 | 不是动态类型；保留显式类型也完全正确 [S1] |
| switch 表达式、箭头分支 | Java 14 | 基础菜单完成后选讲，不作为第一周要求 | 区分语句与返回值表达式，不与模式匹配混称 [S1] |
| 文本块 | Java 15 | 第 3–6 周菜单稳定后选做改写 | 用三引号写多行文本，不当字符串插值 [S1] |
| Record | Java 16 | 第 12–13 周 DTO/商品摘要对比 | 是简洁数据载体；无常规 setter；引用组件的内部对象仍可能可变 [S1][S2] |
| instanceof 模式匹配 | Java 16 | 面向对象基本任务通过后短例子，识读即可 | 减少显式强转，不为了演示强行改业务设计 [S1] |
| sealed 类/接口 | Java 17 | 基础达标后的教师演示或附录 | 理解限制继承范围，不要求项目引入继承层次 [S1] |
| 有序集合统一 API（Sequenced Collections） | Java 21 | 集合基本任务通过后选做 | 了解首尾访问和 reversed 视图；不把“有顺序”误认为“自动排序” [S3] |
| switch 模式匹配 | Java 21 | Web/框架阶段小例子，选做 | 认识按类型匹配；基础菜单不需要此特性 [S1] |
| Record Patterns | Java 21 | Web/框架阶段选做 | 认识 record 数据解构；不作为 Boot 前置 [S1] |
| 虚拟线程 | Java 21 | HTTP 基础完成后教师短演示/选做 | 理解大量等待型任务的并发场景；不是更快的 CPU 线程，也不保证线程安全 [S4] |

### 为什么不集中开一周“所有 Java 21 新特性”

建议每周最多引入 1–2 个有用的新语法，每项完成“Java 8 写法 → 新写法 → 适用边界”的小对比。这样既能交代新特点，也不让语法清单挤掉项目练习。

## 3. 在 Java 21 中仍是预览的内容

本课程不依赖：String Templates、Unnamed Patterns and Variables、Unnamed Classes and Instance Main Methods，以及 Structured Concurrency（结构化并发）。前面三项的状态见 Java 21 语言汇总，结构化并发的状态见 Java 21 官方核心库文档 [S1][S10]。

教师可以用 3 分钟说明“预览不是正式长期承诺”；学生不必配置 `--enable-preview`，不使用网上需要该参数的示例作为主项目基础。不要将本课程锁定的 Java 21 API 与更高 JDK 的同名 API 混写。

## 4. 双环境与迁移边界

- 第一周由教师辅助确认终端运行 JDK、编译 JDK、编辑器当前项目 JDK；只看到终端显示 21 不足以确认编辑器也一致。
- 学校要求 Java 8 的作业继续保持 Java 8 语言级别，不把拓展课的文本块、Record 复制过去。
- 不设置系统全局 JDK 之前先记录学校环境；优先使用项目级配置或单独的终端会话。
- 第 6 周引入 Maven 时，项目明确设置编译 release 为 21，统一 UTF-8；教师提供配置并示范如何看构建结果。
- “本项目在 JDK 21 编译运行”不等于“已完成大型 Java 8 老系统迁移”。本课不承担完整兼容性审计。

## 5. Spring Boot 与 MyBatis 选型说明

**新开课暂选 JDK 21 + Spring Boot 4.1.x + MyBatis Spring Boot Starter 4.0.x。** Boot 4.1 官方系统要求支持 Java 21；MyBatis 官方兼容表把 Starter 4.0 系列对应到 Boot 4.0+ [S6][S13]。这只是讨论中的版本线路，不代表已经完成实际工程验证，也不声称某个补丁是最新。

重要日期：Spring 官方在 **2026-06-25** 的 3.5.16 发布公告中宣布这是 3.5.x 最后一次 OSS 发布，建议需要继续 OSS 支持的项目升级 4.0.x/4.1.x [S12]。当前共备日期为 **2026-10-12**，所以不能把 3.5.x 作为仍持续免费维护的默认新项目基线。商业支持另行安排，不属于本教学预算假设。

若教师已有成熟 Boot 3 教材，可在本地教学对照中使用 **JDK 21 + Boot 3.5.x + Starter 3.0.x**；官方兼容表支持这个技术配对，但兼容性不等于仍获得 OSS 支持 [S5][S6][S12]。采用该备选时明确本地教学限制，不建议公网部署。不要混用两代教程中的依赖、包名和测试配置。

开课前教师必须：

1. 按开课时间再检查支持状态和实际依赖，优先验证 4.1.x；只有明确的旧教材约束才采用 3.5.x 对照备选。
2. 锁定一个具体 Boot 补丁版本和匹配的 MyBatis Starter 补丁版本，不用“3.2+”这种开放范围。
3. 在教学机跑通“启动、连接数据库、一个查询、一项测试、打包”后，向全组发同一模板；JSON/测试依赖以该代官方模板为准，不手抄不同主版本的教程组合。
4. 本轮周期内不随意升级主版本；补丁更新先由教师验证。

Boot 3 教材中的 Servlet/Validation 等 Jakarta EE API 使用 `jakarta.*`；旧 Boot 2 教程可能使用 `javax.*`。只对已迁移的 API 做对比，不说“所有 javax 包都改名”，也不做全局替换 [S8]。

## 6. 官方核对资料

下列地址以原始地址文本存档，供教师在备课时核对。编号用于其他讨论稿的出处标识。

- **[S1] Oracle，Java SE 21 / Java Language Changes Summary**：正式语言特性的版本与 Java 21 预览状态。`https://docs.oracle.com/en/java/javase/21/language/java-language-changes-summary.html`
- **[S2] Oracle，Java SE 21 / Record Classes**：组件、自动生成成员、final 字段与类的限制。`https://docs.oracle.com/en/java/javase/21/language/records.html`
- **[S3] Oracle，Java SE 21 / Creating Sequenced Collections, Sets, and Maps**：JDK 21 有序集合 API。`https://docs.oracle.com/en/java/javase/21/core/creating-sequenced-collections-sets-and-maps.html`
- **[S4] OpenJDK，JEP 444: Virtual Threads；Oracle，Java SE 21 / Virtual Threads**：Java 21 虚拟线程与适用场景。`https://openjdk.org/jeps/444`；备选官方说明：`https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html`
- **[S5] Spring Boot 3.5 / System Requirements**：JDK、构建工具兼容性。`https://docs.spring.io/spring-boot/3.5/system-requirements.html`
- **[S6] MyBatis Spring Boot Starter / Introduction / Requirements**：Starter 与 Boot 的版本配对表。`https://mybatis.org/spring-boot-starter/mybatis-spring-boot-autoconfigure/`
- **[S7] Spring Boot 官方项目页**：查看官方列出的项目线路，不把某条线路默认等同于当前最新版。`https://spring.io/projects/spring-boot/`
- **[S8] Spring 官方仓库 / Spring Boot 3.0 Migration Guide**：Java 基线与 Jakarta EE 包名迁移。`https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide`
- **[S9] Oracle，What’s New in Oracle JDK 9 / JEP 269**：集合工厂方法。`https://docs.oracle.com/javase/9/whatsnew/`
- **[S10] Oracle，Java SE 21 / Structured Concurrency**：Java 21 的预览 API 状态。`https://docs.oracle.com/en/java/javase/21/core/structured-concurrency.html`
- **[S11] Spring Boot / Build / Create an Executable JAR with Maven**：可执行包与构建插件；须选择与最终项目一致的文档代际。`https://docs.spring.io/spring-boot/how-to/build.html`

- **[S12] Spring 官方，Spring Boot 3.5.16 available now（2026-06-25）**：明确说明 3.5.x 最后一次 OSS 发布与建议迁移的线路。`https://spring.io/blog/2026/06/25/spring-boot-3-5-16-available-now/`
- **[S13] Spring Boot 4.1 / System Requirements**：新开课候选的 JDK 与构建工具兼容性；版本文档地址可能重定向到该代当前文档。`https://docs.spring.io/spring-boot/4.1/system-requirements.html`

教学流程、课时和评价标准是本次共备建议，不是上述技术文档的官方教学要求。



