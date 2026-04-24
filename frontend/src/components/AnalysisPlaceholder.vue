<script setup lang="ts">
import {
  Empty,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "./ui/empty";
import { Ghost } from "lucide-vue-next";
import { motion } from "motion-v";

const variantClasses = {
  initial: { opacity: 0, y: 20, scale: 0.95 },
  animate: { opacity: 1, y: 0, scale: 1 },
  exit: { opacity: 0, y: 20, scale: 0.95 },
  transition: { type: "spring", stiffness: 300, damping: 20 } as const,
};
</script>

<template>
  <motion.div
    layout
    class="w-full max-w-3xl mx-auto mt-8 space-y-6 bg-background"
    :initial="variantClasses.initial"
    :animate="variantClasses.animate"
    :exit="variantClasses.exit"
    :transition="variantClasses.transition"
  >
    <Empty
      class="w-full max-w-3xl h-full max-h-2xl mx-auto border border-dashed mt-15"
    >
      <EmptyHeader class="py-30">
        <EmptyMedia variant="icon">
          <Ghost />
        </EmptyMedia>
        <EmptyTitle class="text-2xl font-bold text-foreground">
          No Analysis Yet
        </EmptyTitle>
        <EmptyDescription class="text-muted-foreground">
          Upload your resume to see the analysis results here.
        </EmptyDescription>
      </EmptyHeader>
    </Empty>
  </motion.div>
</template>
