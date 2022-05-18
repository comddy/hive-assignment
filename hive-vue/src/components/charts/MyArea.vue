<template>
  <div>
    <div id='area' style="width:960px;height: 500px"></div>
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
      this.chart = this.$echarts.init(document.getElementById('area'))
      // 指定图表的配置项和数据
      let myChart = this.chart
      myChart.showLoading()
      this.myOption = {
        title: {
          text: '贵州游戏用户密度',
          sublink:
          'http://zh.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E8%A1%8C%E6%94%BF%E5%8D%80%E5%8A%83#cite_note-12'
        },
        tooltip: {
          trigger: 'item'
        },
        toolbox: {
          show: true,
          orient: 'vertical',
          left: 'right',
          top: 'center',
          feature: {
            dataView: { readOnly: false },
            restore: {},
            saveAsImage: {}
          }
        },
        visualMap: {
          min: 3000,
          max: 3500,
          text: ['High', 'Low'],
          realtime: false,
          calculable: true,
          inRange: {
            color: ['lightskyblue', 'yellow', 'orangered']
          }
        },
        series: [
          {
            name: '贵州用户密度',
            type: 'map',
            map: 'HK',
            label: {
              show: true
            },
            data: this.value
          }
        ]
      }
      this.$axios.get('http://localhost:8080/static/520000_full.json'
      ).then(resp => {
        myChart.hideLoading()
        this.$echarts.registerMap('HK', resp.data)
        this.chart.setOption(this.myOption)
      })
    },
    dataHandler () {
      this.$axios.get('/area'
      ).then(resp => {
        let _data = resp.data
        this.name = _data.name
        let length = _data.name.length
        let data = []
        for (var i = 0; i < length; i++) {
          data.push({
            value: _data.value[i],
            name: _data.name[i]
          })
        }
        this.value = data
        this.charts()
      })
    }
  }
}
</script>
