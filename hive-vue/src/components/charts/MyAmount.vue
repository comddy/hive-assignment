<template>
  <div>
    <div id='amount' style="width:600px;height: 300px"></div>
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
      this.chart = this.$echarts.init(document.getElementById('amount'))
      // 指定图表的配置项和数据
      this.myOption = {
        title: {
          text: '游戏玩家充值top10'
        },
        legend: [],
        tooltip: {
        },
        toolbox: {
        },
        grid: {
          top: '10%'
        },
        xAxis: {
          type: 'value',
          name: '元'
        },
        yAxis: {
          type: 'category',
          data: this.name
        },
        series: [
          {
            type: 'bar',
            data: this.value,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'right'
                }
              }
            }
          }
        ]
      }
      this.chart.setOption(this.myOption)
    },
    dataHandler () {
      this.$axios.get('/topN/amount'
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
