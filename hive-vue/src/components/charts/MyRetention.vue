<template>
  <div>
    <div id='retention' style="width:600px;height: 300px"></div>
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
      this.chart = this.$echarts.init(document.getElementById('retention'))
      // 指定图表的配置项和数据
      this.myOption = {
        title: {
          text: '每日留存率'
        },
        tooltip: {
          trigger: 'item'
        },
        toolbox: {
          show: true
        },
        series: [
          {
            name: 'Area Mode',
            type: 'pie',
            radius: [20, 140],
            center: ['50%', '70%'],
            roseType: 'area',
            itemStyle: {
              borderRadius: 5
            },
            data: this.value
          }
        ]
      }
      this.chart.setOption(this.myOption)
    },
    dataHandler () {
      this.$axios.get('/retention'
      ).then(resp => {
        let _data = resp.data
        this.name = _data.name
        let length = _data.name.length
        let data = []
        for (var i = 0; i < length; i++) {
          var value = _data.value[i] * 100
          data.push({
            'value': _data.value[i],
            'name': _data.name[i] + '\n' + value + '%'
          })
        }
        this.value = data
        this.charts()
      })
    }
  }
}
</script>
