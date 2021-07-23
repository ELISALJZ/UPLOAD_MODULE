<template>
  

<el-upload
  class="upload-demo"
  ref="upload"
  action="/api/upload"
  :on-preview="handlePreview"
  :on-remove="handleRemove"
  :file-list="fileList"
  :on-success="handleSuccess"
  :on-error="handleError"
  :auto-upload="false">
  <el-button slot="trigger" size="small" type="primary">Select file</el-button>
  <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">Upload</el-button>
  <div slot="tip" class="el-upload__tip">jpg/png file only</div>
</el-upload>
</template>

<script>
  export default {
   
    methods: {
      handleSuccess(response){
        if (response.errno === 0) {
          this.$message.success(response.errMsg)
        }
      },
      handleError(err){
        const {errno, errMsg} = JSON.parse(err.message)
        if (errno === -1) {
          this.$message.warning(errMsg)
        }
      },
      submitUpload() {
        this.$refs.upload.submit();
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePreview(file) {
        console.log(file);
      }
    }
  }
</script>