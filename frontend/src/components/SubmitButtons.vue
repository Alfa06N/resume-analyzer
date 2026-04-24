<script setup lang="ts">
import { motion, AnimatePresence } from "motion-v";
import { useAnalysisStore } from "@/stores/analysis";
import Button from "./ui/button/Button.vue";
import { Spinner } from "./ui/spinner";

const props = defineProps<{
  jobDescription: string;
  selectedFile: File | null;
}>();

const store = useAnalysisStore();

const startAnalysis = () => {
  store.result = null;
  store.error = null;
  store.analyzeResume(props.selectedFile!, props.jobDescription);
};
</script>

<template>
  <div
    class="flex gap-2 w-full overflow-hidden justify-center items-center py-1 px-1"
  >
    <AnimatePresence mode="popLayout">
      <motion.div
        v-if="store.result || store.error"
        key="reset-wrapper"
        layout
        :initial="{ width: 0, opacity: 0, scaleX: 0, originX: 0 }"
        :animate="{ width: '100%', opacity: 1, scaleX: 1 }"
        :exit="{ width: 0, opacity: 0, scaleX: 0 }"
        :transition="{ type: 'spring', stiffness: 400, damping: 35 }"
        class="flex-1"
      >
        <Button
          variant="outline"
          @click="store.reset"
          :disabled="store.loading"
          class="w-full whitespace-nowrap !transition-none"
        >
          Clear {{ store.result ? "Results" : "Error" }}
        </Button>
      </motion.div>
    </AnimatePresence>

    <motion.div
      layout
      key="analyze-wrapper"
      class="flex-1"
      :animate="{
        flex: store.result || store.error ? 1 : 2,
      }"
      :transition="{ type: 'spring', stiffness: 400, damping: 35 }"
    >
      <Button
        @click="startAnalysis"
        class="w-full"
        :disabled="
          store.loading || !props.selectedFile || !props.jobDescription
        "
      >
        <Spinner v-if="store.loading" class="mr-2" />
        {{ store.loading ? "Analyzing..." : "Analyze Match" }}
      </Button>
    </motion.div>
  </div>
</template>
