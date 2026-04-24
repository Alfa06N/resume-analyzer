<script setup lang="ts">
import { Alert, AlertDescription, AlertTitle } from "./ui/alert";
import { useAnalysisStore } from "@/stores/analysis";
import { storeToRefs } from "pinia";
import { AlertCircleIcon } from "lucide-vue-next";
import { AnimatePresence, motion } from "motion-v";

const store = useAnalysisStore();
const { error } = storeToRefs(store);
const variantClasses = {
  initial: { opacity: 0, y: -10 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -10 },
  transition: { type: "spring", stiffness: 300, damping: 20 } as const,
};
</script>

<template>
  <AnimatePresence mode="wait">
    <motion.div
      class="mb-4 max-w-3xl mx-auto"
      v-if="error"
      :initial="variantClasses.initial"
      :animate="variantClasses.animate"
      :exit="variantClasses.exit"
      :transition="variantClasses.transition"
    >
      <Alert variant="destructive">
        <AlertCircleIcon />
        <AlertTitle>Unable to Process Request</AlertTitle>
        <AlertDescription>{{ error }}</AlertDescription>
      </Alert>
    </motion.div>
  </AnimatePresence>
</template>
