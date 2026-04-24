<script setup lang="ts">
import { ref } from "vue";
import { useFileDialog, useDropZone } from "@vueuse/core";
import { Card, CardContent, CardTitle, CardHeader } from "./ui/card";
import { Textarea } from "./ui/textarea";
import { Label } from "./ui/label";
import SubmitButtons from "./SubmitButtons.vue";
import {
  Tooltip,
  TooltipProvider,
  TooltipContent,
  TooltipTrigger,
} from "./ui/tooltip";
import { InfoIcon } from "lucide-vue-next";

const jobDescription = ref("");
const selectedFile = ref<File | null>(null);

// Dropzone setup
const dropZoneRef = ref<HTMLElement | null>(null);
const { isOverDropZone } = useDropZone(dropZoneRef, (files) => {
  if (files && files[0].type === "application/pdf") {
    selectedFile.value = files[0];
  }
});

// File picker setup
const { open, onChange } = useFileDialog({
  accept: "application/pdf",
  multiple: false,
});

onChange((files) => {
  if (files && files[0]) {
    selectedFile.value = files[0];
  }
});
</script>

<template>
  <Card class="w-full max-w-3xl mx-auto mt-10">
    <CardHeader>
      <CardTitle class="text-2xl font-bold">Resume AI Analyzer</CardTitle>
    </CardHeader>
    <CardContent class="space-y-6">
      <div
        ref="dropZoneRef"
        @click="open()"
        :class="[
          'border-2 border-dashed rounded-lg p-10 text-center cursor-pointer transition-colors',
          isOverDropZone
            ? 'border-primary bg-primary/10'
            : 'border-muted-foreground/25',
        ]"
      >
        <div v-if="!selectedFile">
          <p class="text-lg font-medium">Drag your resume PDF here</p>
          <p class="text-sm text-muted-foreground">or click to browse</p>
        </div>
        <div v-else class="text-primary font-semibold">
          📄 {{ selectedFile.name }}
        </div>
      </div>

      <div class="space-y-2">
        <div class="flex w-full justify-between items-center gap-2">
          <Label htmlFor="description">Job Description</Label>

          <TooltipProvider>
            <Tooltip :delayDuration="300">
              <TooltipTrigger asChild>
                <InfoIcon class="h-4 w-4 text-muted-foreground cursor-help" />
              </TooltipTrigger>
              <TooltipContent class="max-w-[250px]">
                <p>
                  Type <code class="font-bold">DEMO</code> to see a simulated
                  analysis and explore the results dashboard without consuming
                  AI credits.
                </p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
        </div>
        <Textarea
          class="h-32 max-h-64 min-h-32"
          v-model="jobDescription"
          placeholder="Paste the job requirements here..."
        ></Textarea>
      </div>

      <SubmitButtons
        :job-description="jobDescription"
        :selected-file="selectedFile"
      />
    </CardContent>
  </Card>
</template>
