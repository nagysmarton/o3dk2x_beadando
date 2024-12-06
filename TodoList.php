<?php

class TodoList
{
    private array $tasks = [];

    public function addTask(string $task): void
    {
        $this->tasks[] = $task;
    }

    public function getTasks(): array
    {
        return $this->tasks;
    }

    public function clearTasks(): void
    {
        $this->tasks = [];
    }
}
