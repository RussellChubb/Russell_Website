---
title: "File Permissions"
description: "Introduction to File Permissions in Linux"
summary: "Introduction to File Permissions in Linux"
showAuthor: true
date: 2026-05-09
featureimage: "featured.jpg"
tags: ["Linux"]
series: ["Learn Linux"]
series_order: 42
weight: -42
---

You've likely clicked this video for two reasons:

1. You've just executed `ls -l` into your terminal and now it feels like you're trying to read Minecraft Enchanting language.
2. You're a cool person, and you want to learn a little bit about file permissions (and how to alter them).

Let's start with the basics — in Linux, every file and directory has a set of permissions that determine who can read, write, or execute them.

This is where the `ls -l` command comes in...

As you know from my previous video, `ls -l` returns a long listing format of the files in our current directory, which includes a 10 character string called the security "mode" of a file.

This "security mode" is the basis for understanding a file, or directory's permission settings. Let's start with the first character of the "security mode", which represents the type of file:

- `-` — Regular file
- `d` — Directory
- `l` — Symbolic link

The next nine characters in the security mode are the permissions, divided into three sections:

| Section | Represents |
|---------|------------|
| 1st     | Owner's permissions |
| 2nd     | Group's permissions |
| 3rd     | Others' permissions |

In the context of file permissions:

- **Owner** `(u)` — The user who owns the file.
- **Group** `(g)` — A set of users that share the same permissions.
- **Others** `(o)` — Everyone else.

Each of these groups has three types of permissions:

| Permission | Symbol | Description                               |
|------------|--------|-------------------------------------------------- |
| Read       | `r`    | Allows you to read the contents of a file |
| Write      | `w`    | Allows you to modify a file |
| Execute    | `x`    | Allows you to execute the file as a program |

---

## Modifying Permissions with `chmod`

You can modify these permissions using the `chmod` command (which stands for "change mode").

For example, to give **execute** permissions to the **other** group for the directory `test`:

```bash
chmod o+x test
```

- `o` — targets the "other" group
- `+` — adds a permission
- `x` — the "execute" permission
- `test` — the directory being updated

You can also change multiple groups' permissions in a single command. For example, the following will add read and write permissions to both the user and group, while also revoking the execute permission from others, for the file `demo_file.txt`:

```bash
chmod ug+rw,o-x demo_file.txt
```

---

That's it for my rundown on file permissions in Linux! If you like the video, like the video. If you want to see more of me, press subscribe.

Thanks for watching, and I'll see you in the next one!
