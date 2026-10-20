# Lesson 01: Java Basics

创建日期：2026-10-18  
课程形式：腾讯会议线上课  
建议人数：10 人  
建议时长：90 分钟

## 课程目标

本节课不追求讲完 Java 基础，只建立进入下一节 WorkBuddy AI 协作课前的最低能力线：

> 学生能独立打开并运行一个 Java 小程序，定位输入、分支、循环、方法和 `List` 遍历，完成一个 3-8 行的局部修改，并用正常、异常、边界输入验证结果。

本节课不讲 WorkBuddy 操作、Git 团队协作、Maven、完整面向对象设计、数据库、Spring Boot 或 Java 21 新语法。

## 目录说明

```text
lesson-01-java-basics/
├── README.md
├── 00-课程方案.md
├── student/                         # 可直接发给学生
│   ├── 00-课前检查清单.md
│   ├── 01-Java基础速查.md
│   ├── 02-课堂练习单.md
│   ├── 03-自测与离场票.md
│   ├── starter/WarehouseBasics.java
│   └── expected-output/*.txt
├── teacher/                         # 教师专用，不随学生包发放
│   ├── 01-教师执行稿.md
│   ├── 02-微诊断答案与分层.md
│   ├── 03-八页演示稿.md
│   ├── 04-常见错误处理卡.md
│   ├── 05-课后补练卡.md
│   ├── 06-学生能力矩阵.csv
│   └── answer/WarehouseBasics.java
├── tools/
│   └── verify.ps1
├── lesson-01-java-basics-student.zip # 可直接发给学生
└── 交付检查记录.md
```

## 教师开课前操作

1. 运行 `tools/verify.ps1`，确认骨架和答案都能编译，答案通过 8 个行为场景。
2. 将 `lesson-01-java-basics-student.zip` 发给学生，不发 `teacher` 文件夹。
3. 提前一天收集课前检查结果；环境问题单独处理，不占主课时间。
4. 打开 `teacher/01-教师执行稿.md` 和 `teacher/03-八页演示稿.md` 作为课堂主控材料。
5. 复制 `teacher/06-学生能力矩阵.csv`，填入学生姓名。

## 运行方式

在 `student/starter` 目录执行：

```powershell
javac -encoding UTF-8 WarehouseBasics.java
java WarehouseBasics
```

骨架在未完成 TODO 时也能编译，但行为不完整。学生应按练习顺序完成四个 TODO，不要直接替换成教师答案。

## 过关标准

学生至少应做到：

- 本人能启动、停止并再次运行程序；
- 能指出输入、分支、循环、方法调用和 `List` 遍历的位置；
- 菜单可重复，`0` 正常退出，未知输入后仍可继续；
- 搜索支持部分匹配和大小写忽略，空关键字不会匹配全部内容；
- 独立完成一项局部修改；
- 留下至少 5 个真实测试场景的预期与实际结果。

