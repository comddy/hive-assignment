<template>
  <div>
    <div id='login' style="width:600px;height: 300px"></div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      chart: '',
      myOption: '',
      name: [],
      new: [],
      old: []
    }
  },

  mounted () {
    this.dataHandler()
  },

  methods: {
    charts () {
      // 基于准备好的dom，初始化echarts实例
      this.chart = this.$echarts.init(document.getElementById('login'))
      // 指定图表的配置项和数据
      this.myOption = {
        title: {
          text: '每日登录注册'
        },
        legend: {
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        toolbox: {
        },
        grid: {
          top: '15%',
          left: '15%'
        },
        xAxis: {
          type: 'category',
          data: this.name,
          axisLabel: {
            rotate: 60
          }
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            type: 'bar',
            data: this.new,
            name: '新用户',
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'
                }
              }
            }
          },
          {
            type: 'bar',
            data: this.old,
            name: '老用户',
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'
                }
              }
            }
          }
        ]
      }
      this.chart.setOption(this.myOption)
    },
    dataHandler () {
      this.$axios.get('/dailyLogin'
      ).then(resp => {
        let _data = resp.data
        this.name = _data.name
        this.new = _data.new
        this.old = _data.old
        this.charts()
      })
    }
  }
}
</script>
