一个月复习完一门
2019.10.24开始复习财务第二章，计划于2019.11.24前复习完整本财管


@echo off
Setlocal enabledelayedexpansion

Set "BeforeStr=被替换的内容"
Set "AfterStr=新内容"

For /r %%# in (*) Do (
    Set "File=%%~nx#"
    Ren "%%#" "!File:%BeforeStr%=%AfterStr%!"
)

Pause&Exit
