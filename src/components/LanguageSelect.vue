<template>
  <v-select
    label="Deck Language"
    prepend-icon="mdi-translate"
    v-model="language"
    @input="change"
    :items="languages"
    dense
    filled
  />
</template>

<script>
export default {
  name: "LanguageSelect",

  props: {
    value: String,
  },

  data: () => ({
    language: "",

    languages: [
      { value: "en", text: "English" },
      { value: "fr", text: "French" },
      { value: "de", text: "German" },
      { value: "it", text: "Italian" },
      { value: "ja", text: "Japanese" },
      { value: "es", text: "Spanish" },
    ],
  }),

  mounted() {
    this.language = this.value;

    this.$emit("input", this.current_language);
  },

  computed: {
    language_values() {
      var res = [];

      for (const lang of this.languages) {
        res.push(lang.value);
      }

      return res;
    },

    current_language() {
      if (this.language_values.includes(this.language)) {
        return this.language;
      } else {
        return "en";
      }
    },
  },

  methods: {
    change() {
      this.$emit("input", this.current_language);
    },
  },
};
</script>
