<template>
  <div>
    <div id='time' style="width:600px;height: 300px"></div>
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
      this.chart = this.$echarts.init(document.getElementById('time'))
      // 指定图表的配置项和数据
      this.myOption = {
        title: {
          text: '游戏时间top10'
        },
        legend: [],
        tooltip: {
        },
        toolbox: {
        },
        grid: {
          top: '15%'
        },
        xAxis: {
          type: 'value',
          name: '小时'
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
      this.$axios.get('/topN/time'
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
