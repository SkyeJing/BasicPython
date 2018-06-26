# coding=utf-8
# 定义一个只包含格式字符的字符串
formatter = "%r %r %r %r"
# 用上面定义的格式字符串，格式化以下类型数据，输出与输入一致，适用于debug。
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)