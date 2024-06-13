import streamlit as st
import pandas as pd
import random

# 读取Excel文件中的笑话数据
def load_jokes():
    df = pd.read_excel(r'C:\Users\田六六\Desktop\Dataset4JokeSet.xlsx')  
    df.columns = ['Joke']
    jokes = df['Joke'].tolist()
    return jokes

def show_jokes_and_get_ratings(jokes, num_jokes,title="初始笑话",prefix=""):
    ratings = []
    for i in range(num_jokes):
        joke_key = f"{prefix}joke{i+1}_rating" 
        st.write(f"{title} {i+1}: {jokes[i]}")
        rating = st.slider(f"给笑话 {i+1} 打分", -10, 10, 0,key=joke_key)
        ratings.append(rating)
    return ratings

def calculate_average(ratings):
    if ratings:
        return sum(ratings) / len(ratings)
    return 0

def main():
    st.title("笑话评分与推荐系统")
    
    all_jokes = load_jokes()
    
    # 随机选择3个初始笑话
    initial_jokes = random.sample(all_jokes, 3)
    initial_ratings = show_jokes_and_get_ratings(initial_jokes, 3,title="推荐笑话",prefix="initial")
    
    if st.button("Submit Ratings"):
        st.success("评分已提交！")
        
        # 基于初始评分推荐5个笑话
        recommended_jokes = random.sample(all_jokes, 5)
        recommend_ratings = show_jokes_and_get_ratings(recommended_jokes, 5,prefix="recommended")
        
        if st.button("Submit Recommend Ratings"):
            st.success("推荐笑话评分已提交！")
            
            # 计算推荐笑话的平均满意度
            satisfaction = calculate_average(recommend_ratings)
            st.write(f"本次推荐的用户满意度为：{satisfaction:.2f}")

def main():
    st.title("笑话评分与推荐系统")
    
    all_jokes = load_jokes()
    
    # 初始化展示和评分相关的状态
    initial_jokes_shown = False
    recommendations_given = False
    
    # 主循环确保页面不自动刷新至初始状态
    while True:
        if not initial_jokes_shown:
            # 随机选择3个初始笑话
            initial_jokes = random.sample(all_jokes, 3)
            initial_ratings = show_jokes_and_get_ratings(initial_jokes, 3, title="初始笑话", prefix="initial")
            
            if st.button("Submit Ratings"):
                st.success("评分已提交！")
                initial_jokes_shown = True
        
        elif not recommendations_given and initial_jokes_shown:
            # 基于初始评分推荐5个笑话
            recommended_jokes = random.sample(all_jokes, 5)
            recommend_ratings = show_jokes_and_get_ratings(recommended_jokes, 5, title="推荐笑话", prefix="recommended")
            
            if st.button("Submit Recommend Ratings"):
                st.success("推荐笑话评分已提交！")
                recommendations_given = True
                
                # 计算推荐笑话的平均满意度
                satisfaction = calculate_average(recommend_ratings)
                st.write(f"本次推荐的用户满意度为：{satisfaction:.2f}")
        
        # 当所有环节完成，跳出循环以防止无限循环
        if initial_jokes_shown and recommendations_given:
            break





if __name__ == "__main__":
    main()