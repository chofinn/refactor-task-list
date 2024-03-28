## 改動
### HW2
- 將各項 command 抽成一個 class 並獨立放在一個檔案
- 把只有某個 command 會用到的 function 放在他自己的 class 裡
- 新增一個 CommandInterface 讓所有 command class 繼承它，並把它和各項 command 及放到同一個資料夾
- 執行 command 改為 strategy 的方式來執行
- console 和 task 用參數的方式傳給需要用到的 command
- 把 command.py 裡的 command_rest 變數改成 command 跟 args
- 為 add command 增加更完整的參數檢查

### HW3
- 將整個程式分成四層 (entities, use cases, adapters, io)
- 新增 tasklist 類別
- command 會將欲輸出字串回傳，而非直接印出
