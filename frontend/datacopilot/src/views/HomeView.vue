<template>
<!--  布局 -->
  <div>
    <el-container>
      <el-header>
        <el-menu
            :default-active="activeIndex"
            :ellipsis="false"
            mode="horizontal"
        >
          <img alt="DataCopilot" fit="fill" src="@/assets/DataCopilot.svg" style="height: 100%"/>
          <el-menu-item index="0" @click="goToHome"><el-icon :size="20" color="#000000"><House/></el-icon>主页</el-menu-item>
          <el-menu-item ref="ref3" index="1" @click="goToDatabase"><el-icon :size="20" color="#000000"><Coin/></el-icon>数据库</el-menu-item>
          <el-menu-item ref="ref4" index="2" @click="goToQuery"><el-icon :size="20" color="#000000"><Search/></el-icon>查询</el-menu-item>
          <div class="flex-grow"/>
          <el-menu-item v-if="!username" ref="ref2" index="3" @click="goToLogin"><el-icon :size="20" color="#000000"><UserFilled/></el-icon>登陆</el-menu-item>
          <el-menu-item v-if="!username" ref="ref1" index="4" @click="goToRegister"><el-icon :size="20" color="#000000"><User/></el-icon>注册</el-menu-item>
          <el-menu-item v-if="username" index="5" @click="goToUser"><el-icon :size="20" color="#000000"><UserFilled/></el-icon>{{ username }}</el-menu-item>
          <el-menu-item v-if="username" ref="ref6" index="6" @click="logout"><el-icon :size="20" color="#000000"><SwitchButton/></el-icon>退出</el-menu-item>
        </el-menu>
      </el-header>

      <!--      页面主要部分  -->
      <el-main>
        <!-- 醒目的大标题 -->
        <div class="main-title">
          <p class="title">DataCopilot</p>
          <!-- 介绍文字 -->
        <div class="introduction">
          <p>探索DataCopilot，一款革命性的网页应用，它通过采用尖端的大模型技术，为用户带来了前所未有的数据库查询和数据可视化体验。</p>
        </div>
        </div>

        <div class="container">
          <div class="typed-out"><el-icon :size="20" color="#FFFFFF" style="margin-right: 10px"><Search/></el-icon> 帮我查询一下李华同学的成绩</div>
        </div>
        <div class="container">
          <div class="typed-out"><el-icon :size="20" color="#FFFFFF" style="margin-right: 10px"><MagicStick/></el-icon>SQL: SELECT * FROM students WHERE name = '李华'</div>
        </div>
        <div class="button-container">
          <el-button class="big-rounded-button" style="background-color:#CD6CE7;" @click="open = true">
            <el-icon :size="20" color="#FFFFFF" style="margin-right: 10px"><Compass/></el-icon>
              查看引导
          </el-button>
          <el-button class="big-rounded-button" style="background-color:#FFDF58;" @click="goAhead">
            立即体验
          <el-icon :size="20" color="#FFFFFF" style="padding-left: 10px;"><TopRight/></el-icon>
          </el-button>
        </div>
      </el-main>
      <el-tour v-if="!username" v-model="open">
        <el-tour-step :target="ref1?.$el" description="在这里，您可以创建一个新的账号，开始您的DataCopilot之旅。填写必要的信息并设置一个安全的密码。"
                      title="1、创建一个账号"/>
        <el-tour-step :target="ref2?.$el" description="使用您刚创建的账号信息登录DataCopilot平台。如果您已经拥有账号，请直接输入您的用户名和密码进行登录。"
                      title="2、登陆账号"/>
        <el-tour-step :target="ref3?.$el" description="登录后，您需要添加可以访问的数据库。选择您的数据库类型，输入连接信息，并确保您有权限访问所选数据库。"
                      title="3、添加数据库"/>
        <el-tour-step :target="ref4?.$el" description="现在您可以使用DataCopilot的强大查询功能了。通过自然语言处理技术，您可以用简单的问题形式来查询数据库，而无需编写复杂的SQL语句。您还可以通过可视化工具来展示查询结果。"
                      title="4、进行查询"/>
      </el-tour>
      <el-tour v-if="username" v-model="open">
        <el-tour-step :target="ref3?.$el" description="登录后，您需要添加可以访问的数据库。选择您的数据库类型，输入连接信息，并确保您有权限访问所选数据库。"
                      title="1、添加数据库"/>
        <el-tour-step :target="ref4?.$el" description="现在您可以使用DataCopilot的强大查询功能了。通过自然语言处理技术，您可以用简单的问题形式来查询数据库，而无需编写复杂的SQL语句。您还可以通过可视化工具来展示查询结果。"
                      title="2、进行查询"/>
      </el-tour>
    </el-container>
  </div>
</template>

<script>
import {ref} from 'vue'
export default {
  data() {
    return {
      activeIndex: '0', // 默认激活的菜单项
      open: false,
      username: this.$route.query.username || '',
    }
  },
  created() {
    this.username = this.$route.query.username;
  },
  setup() {
    // 使用ref创建响应式引用
    const ref1 = ref(null);
    const ref2 = ref(null);
    const ref3 = ref(null);
    const ref4 = ref(null);
    return {
      ref1,
      ref2,
      ref3,
      ref4,
    };
  },
  methods: {
    goToHome() {
      this.$router.push({path: '/', query: {username: this.username}});
    },
    goToLogin() {
      this.$router.push('/login');
    },
    goToRegister() {
      this.$router.push('/register');
    },
    goToDatabase() {
      this.$router.push({path: '/database', query: {username: this.username}});
    },
    goToQuery() {
      this.$router.push({path: '/query', query: {username: this.username}});
    },
    goToUser() {
      this.$router.push({path: '/user', query: {username: this.username}});
    },
    logout() {
      this.username = '';
    },
    goAhead() {
      this.$router.push({path: '/database', query: {username: this.username}});
    },
  }
}
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}

.el-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 使用视口高度作为容器的最小高度 */
}

.el-header {
  flex: 0 1 auto; /* 不占据多余空间，只占据自身所需空间 */
}

.el-main {
  display: flex;
  flex: 1; /* main元素占据剩余空间 */
  overflow: auto; /* 如果内容超出，显示滚动条 */
  flex-direction: column; /* 使子元素垂直排列 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  background: linear-gradient(-40deg, #FFDF58, #CD6CE7, #F7D7A7);
  background-size: 1000% 1000%;
  animation: gradientBG 5s ease infinite;
  padding: 20p x; /* 添加内边距 */

}

@keyframes gradientBG {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.main-title {
  margin: 10px 0 10px 0; /* 标题与介绍文字之间的间距 */
  padding: 0;
}

.title {
  font-size: 8em; /* 增大标题字体大小 */
  color: #FFFFFF; /* 标题颜色 */
  text-align: center; /* 确保标题居中 */
  font-weight: bold; /* 加粗标题 */
  margin: 0 0 30px 0; /* 重置margin */
  padding: 0; /* 重置padding */
}

.introduction {
  max-width: 600px; /* 限制介绍文字的最大宽度 */
  text-align: center;
  margin: auto;
}

.introduction p {
  font-size: 1.2em; /* 增大段落字体大小 */
  color: #FFFFFF; /* 段落颜色 */
  line-height: 2; /* 行高 */
  margin: 0 0 30px 0; /* 段落之间的间距 */

}

.typed-out {
  overflow: hidden;
  border-right: .15em solid orange;
  white-space: nowrap;
  font-size: 1.6rem;
  width: 0;
  animation: typing 1s steps(20, end) forwards,
  blink .8s infinite;
  color: #FFFEE1;
}

@keyframes typing {
  from {
    width: 0
  }
  to {
    width: 100%
  }
}

@keyframes blink {
  from {
    border-color: transparent
  }
  to {
    border-color: orange;
  }
}

.container {
  display: inline-block;
  margin: 10px 0 30px 0;
  text-align: center;
}

.button-container {
  display: flex; /* 使用Flexbox布局 */
  justify-content: center; /* 水平居中 */
  margin: 20px 0; /* 添加外边距 */
}

.big-rounded-button {
  font-size: 20px; /* 增大字体大小 */
  padding: 10px 20px 10px 20px; /* 增大内边距 */
  border-radius: 20px; /* 设置圆角 */
  margin: 0 40px; /* 添加外边距，使按钮之间有间隔 */
  border: none; /* 移除边框 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
  color: white;
}

.big-rounded-button:hover {
  transform: scale(1.05); /* 鼠标悬浮时放大 */
}
</style>