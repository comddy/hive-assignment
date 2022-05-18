<template>
  <body>
    <el-row>
      <el-col :span="24">
        <h2 style="text-align:center">总收入：{{totalAmount}} 元</h2>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12">
        <my-amount></my-amount>
      </el-col>
      <el-col :span="12">
         <my-time></my-time>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12">
        <my-daily-amount></my-daily-amount>
      </el-col>
      <el-col :span="12">
        <my-daily-login></my-daily-login>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12" style="margin-top:50px">
        <my-retention></my-retention>
      </el-col>
      <el-col :span="6" style="margin-top:50px">
        <h3>人均使用时长: {{perTime[0]}} 小时</h3>
      </el-col>
      <el-col :span="6" style="margin-top:50px">
        <h3>次均使用时长: {{perTime[1]}} 小时</h3>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24" style="margin-top:50px" align="center">
        <my-area></my-area>
      </el-col>
    </el-row>
  </body>
</template>

<script>
import MyAmount from './charts/MyAmount.vue'
import MyTime from './charts/MyTime.vue'
import MyDailyAmount from './charts/MyDailyAmount.vue'
import MyDailyLogin from './charts/MyDailyLogin.vue'
import MyRetention from './charts/MyRetention.vue'
import MyArea from './charts/MyArea.vue'
export default {
  components: {MyAmount, MyTime, MyDailyAmount, MyDailyLogin, MyRetention, MyArea},
  data () {
    return {
      totalAmount: 0,
      perTime: []
    }
  },
  mounted () {
    this.$axios.get('/amount/total'
    ).then(resp => {
      this.totalAmount = resp.data
    })
    this.$axios.get('/summary'
    ).then(resp => {
      this.perTime = resp.data.value
    })
  }
}
</script>

<style>

</style>
