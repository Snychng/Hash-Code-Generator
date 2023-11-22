# Password Generator and Validator 🛡️

## 项目描述 📝

这个项目是一个使用 Python 和 Tkinter GUI 库实现的密码生成和验证工具。它可以根据用户指定的日期生成一个密码，并能够验证输入的密码是否与已生成的密码匹配。

## 特性 🔅

1. **密码生成器**：在输入日期后，它将生成一个新的密码，这个密码是通过**哈希函数**和特定的盐值生成的。
2. **密码验证器**：您可以输入一个密码和一个日期，它将确认该密码是否是在指定日期生成的密码。
3. **数据持久性**：生成的密码和盐值会被保存在一个 pickle 文件中，该文件保存最近七天生成的密码。

## 使用指南 🚀

1. 运行 `gui.py` 启动密码生成器和验证器的 GUI。
2. 在 **Date** 文本框中输入一个日期（格式为 "YYYYMMDD"），然后点击 **Generate Password** 按钮生成一个新的密码。
3. 生成的密码将显示在 **Generated Password** 文本框中。
4. 要验证一个密码，输入一个日期和一个密码，然后点击 **Validate Password** 按钮。它将显示一个消息框，告知您密码验证是否成功。

## 文件描述 📂

- `gui.py`：这个文件包含了用于构建 GUI 的代码，主要包括各种标签、按钮和文本框。

- `functions.py`：这个文件包含了用于生成和验证密码的函数，以及用于保存和加载密码数据的函数。

## 代码示例 💻

```python
def on_generate_password(password_entry):
    today = datetime.datetime.now().strftime('%Y%m%d')
    salt = os.urandom(16)
    password = generate_password(today, salt)
    save_password_salt(today, password, salt)
    password_entry.configure(state='normal')
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    password_entry.configure(state='readonly')
```

上述代码示例显示了如何生成一个新密码并保存它。

## 依赖项 ⚙️

- [Python](https://www.python.org/)：Python 语言。
- [Tkinter](https://docs.python.org/3/library/tkinter.html)：Python 的标准 GUI 库。
- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/)：用于美化 Tkinter 应用程序的库。

## 贡献 👥

欢迎任何形式的贡献，包括 bug 报告、功能建议、文档改进，或直接提交代码。

## 许可证 📄

请参阅项目根目录下的 LICENSE 文件。

## 联系 📧

如有任何问题或建议，请通过 issue 提交或通过 email 联系我。

---

感谢您对这个项目的关注！💖

---

⚠️以上内容由GPT-4自动生成。

- 作者邮箱 <snychng@gmail.com>

- 想看作者AI相关的内容分享请点击[👻这里](https://ai.yucheng.life)

- 作者基于[ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web)项目部署的ChatGPT请点击[👻这里](https://chat.yucheng.life)
