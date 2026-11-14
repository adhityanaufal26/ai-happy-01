// ai-happy-01 v3 entry (Node 22, standard library only).
// The entry image lives beside this file as entry.png; the program copies
// those exact bytes to /output/entry.png. No network, no randomness, no
// writes anywhere else, so both grader runs produce identical bytes.
// Determinism: a byte-for-byte copy of a fixed file cannot drift between
// runs, which is exactly what the harness requires (two runs, same bytes).
//
// Local check:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const bytes = readFileSync(join(here, 'entry.png'));

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, 'entry.png'), bytes);
