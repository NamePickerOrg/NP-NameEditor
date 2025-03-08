import streamlit as st
import pandas as pd

names = pd.DataFrame([[0,0,0]],columns=("name","sex","no"))
st.title("NamePicker - 名单编辑器")

def save():
    global names
    names.to_csv("temp.csv",index=False,encoding="utf-8")

def load():
    global names
    names = pd.read_csv("temp.csv")

load()
st.dataframe(names)

tasklist = ["添加一条信息","修改一条信息","移除一条信息"]
sexoption = ["男","女"]
task = st.selectbox("选择要执行的操作",tasklist)
newinfo = [0,0,0]
if task == tasklist[0]:
    newinfo[0] = st.text_input("姓名")
    newinfo[1] = sexoption.index(st.radio("性别",options=sexoption))
    newinfo[2] = st.number_input("学号",min_value=0,step=1)
    if st.button("提交"):
        names.loc[len(names)] = newinfo
        st.success("提交成功")
        save()
        load()
elif task == tasklist[1]:
    target = st.selectbox("需要修改的信息",names)
    newinfo[0] = st.text_input("姓名")
    newinfo[1] = sexoption.index(st.radio("性别", options=sexoption))
    newinfo[2] = st.number_input("学号",min_value=0,step=1)
    if st.button("提交"):
        names.loc[names["name"]==target] = newinfo
        newinfo = [0, 0, 0]
        st.success("提交成功")
        save()
        load()
else:
    target = st.selectbox("需要删除的信息",names)
    if st.button("提交"):
        names.loc[names["name"]==target] = [None,None,None]
        names.dropna(axis=0,how="all",inplace=True)
        st.success("提交成功")
        save()
        load()

down = names.to_csv(index=False,encoding="utf-8")
st.download_button(
    label="下载names.csv",
    data=down,
    file_name="names.csv",
    mime="text/csv",
    icon=":material/download:",
)