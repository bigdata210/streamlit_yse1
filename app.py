# -*- coding:UTF-8 -*-
import streamlit as st

def main():
    # title
    st.title("Hello World")

    # text
    st.text('This is so {}'.format("good"))

    # Header
    st.header("This is Header")

    # Subheader
    st.subheader("This is subHeader")

    # Markdown
    st.markdown("## This is Markdown")

    # 색상이 들어간 텍스트 feature
    st.success('성공')
    st.warning('경고')
    st.info('정보와 관련된 탭')
    st.error('에러 메세지')
    st.exception('예외처리')

    # st.write()
    st.write('일반텍스트')
    st.write(1+2)
    st.write(dir(str))

    st.title(':sunglasses:')

    # Help
    st.help(range)
    st.help(st.title)

if __name__ == '__main__':
    main()