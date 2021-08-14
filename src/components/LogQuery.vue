<template>
  <div id="lq">
    <el-input
      placeholder="请输入键值后点击查询"
      prefix-icon="el-icon-search"
      v-model="input1"
      class="input-with-select"
      clearable
    >
      <template #prepend>
        <el-select v-model="value" placeholder="环境选择"
        default-first-option clearable filterable>
          <el-option v-for="item in EnvList"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
        </el-select>
        <el-select-v2 v-model="item" placeholder="系统选择" clearable
        filterable :options="options" style="width: 130px;" default-first-option/>
      </template>
      <template #append>
        <el-button type="primary" icon="el-icon-search">搜索</el-button>
      </template>
    </el-input>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
export default defineComponent({
  setup () {
    // 系统列表
    const SysList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    // 环境列表
    const EnvList = [{
      value: 'st',
      label: 'st'
    }, {
      value: 'uat',
      label: 'uat'
    }, {
      value: 'pre',
      label: 'pre'
    }]
    const options = Array.from({ length: SysList.length - 1 }).map((_, idx) => ({
      item: `选项${idx + 1}`,
      label: `${SysList[idx]}`
    }))
    return {
      input1: ref(''),
      select: ref(''),
      value: ref(''),
      item: [],
      options,
      EnvList
    }
  }
})
</script>

<style>
.el-select .el-input {
  width: 130px;
}

.input-with-select .el-input-group__prepend {
  background-color: #fff;
  padding-left: 0;
  padding-right: 0;

}
.el-select-v2 {
  margin-inline-start: 15px;
}
</style>
