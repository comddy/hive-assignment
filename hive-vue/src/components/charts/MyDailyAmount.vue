<template>
  <div>
    <div id='daily' style="width:600px;height: 300px"></div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      chart: '',
      myOption: '',
      name: [],
      value: []
    }
  },

  mounted () {
    this.dataHandler()
  },

  methods: {
    charts () {
      // 基于准备好的dom，初始化echarts实例
      this.chart = this.$echarts.init(document.getElementById('daily'))
      // 指定图表的配置项和数据
      this.myOption = {
        title: {
          text: '每日收入'
        },
        legend: [],
        tooltip: {
        },
        toolbox: {
        },
        grid: {
          top: '20%',
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
          type: 'value',
          name: '元'
        },
        series: [
          {
            type: 'bar',
            data: this.value,
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
      this.$axios.get('/amount'
      ).then(resp => {
        let _data = resp.data
        this.name = _data.name
        this.value = _data.value
        this.charts()
      })
    }
  }
}
</script>
