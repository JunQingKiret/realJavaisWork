import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class WarehouseBasics {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> items = Arrays.asList(
                "螺丝刀",
                "Keyboard",
                "打印纸",
                "安全帽"
        );

        boolean running = true;

        while (running) {
            printMenu();
            String choice = scanner.nextLine().trim();

            if ("1".equals(choice)) {
                for (String item : items) {
                    System.out.println(item);
                }
            } else if ("2".equals(choice)) {
                System.out.print("请输入搜索关键字：");
                String keyword = scanner.nextLine().trim();

                if (keyword.isEmpty()) {
                    System.out.println("搜索关键字不能为空。");
                } else {
                    searchItems(items, keyword);
                }
            } else if ("0".equals(choice)) {
                running = false;
                System.out.println("已退出 103 仓库基础练习。");
            } else {
                System.out.println("无效选项：请输入 1、2 或 0。你输入的是：" + choice);
            }
        }

        scanner.close();
    }

    static void printMenu() {
        System.out.println();
        System.out.println("===== 103 仓库基础练习 =====");
        System.out.println("1. 查看所有物品");
        System.out.println("2. 按名称搜索");
        System.out.println("0. 退出");
        System.out.print("请选择：");
    }

    static void searchItems(List<String> items, String keyword) {
        boolean found = false;

        for (String item : items) {
            boolean matches = item.toLowerCase().contains(keyword.toLowerCase());

            if (matches) {
                System.out.println("找到：" + item);
                found = true;
            }
        }

        if (!found) {
            System.out.println("未找到包含“" + keyword + "”的物品。");
        }
    }
}

