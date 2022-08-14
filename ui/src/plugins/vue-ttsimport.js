import Vue from 'vue'

Object.defineProperty(Vue.prototype, "ttsimport_api_baseurl", {
  get: function () {
    if (process.env.NODE_ENV === "production") {
      return "//" + window.location.host + "/api";
    } else {
      if (process.env.NODE_ENV !== "development") {
        console.warn("Unexpected NODE_ENV value");
      }

      return "//" + window.location.hostname + ":5000/api";
    }
  }
});

Object.defineProperty(Vue.prototype, "ttsimport_language", {
  value: "",
  writable: true,
});
