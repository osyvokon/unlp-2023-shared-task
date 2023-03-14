# UNLP 2023 Shared Task in Grammatical Error Correction for Ukrainian

The Second Ukrainian NLP workshop ([UNLP 2023](https://unlp.org.ua/)) organizes the first Shared Task
in Grammatical Error Correction for Ukrainian.

## Updates

**2023-03-14**:

* [Official results](https://github.com/asivokon/unlp-2023-shared-task#results) announced.
* [Leadboard](https://codalab.lisn.upsaclay.fr/competitions/10740) stays active. You are welcome to continue making submissions.

**2023-2-13**:

* [Codalab](https://codalab.lisn.upsaclay.fr/competitions/10740) competition / leaderboard launched
* Private test set available in [Codalab](https://codalab.lisn.upsaclay.fr/competitions/10740)
* Add `./scripts/tokenizer.py`

**2023-01-24**:

* Remove some fluency edits in gec-only

* Fix some error types in .m2 files

* Fix sentence alignment in some rare cases

* Add valid.tgt.{txt,tok}

**2023-01-17**:

* Numerous fixes in whitespace before/after punctuation -- contributed by @danmysak

* Removed the second annotator's annotations from `train.src`/`train.tgt` as they
were causing confusion. These annotations could be found in the original UA-GEC
data or in train.m2 if you really need it.

## Task description

In this shared task, your goal is to correct a text in the Ukrainian language to
make it grammatical or both grammatical and fluent.

There are two tracks in this shared task: GEC-only and GEC+Fluency. It is
**not mandatory** to participate in both subtasks, i.e., participating in
either GEC-only or GEC+Fluency is acceptable.

## Track 1: GEC-only

Grammatical error correction (GEC) is a task of automatically detecting and
correcting grammatical errors in written text. GEC is typically limited to
making a minimal set of grammar, spelling, and punctuation edits so that the
text becomes error-free.

For example:
```
Input:  Я йти до школи.
Output: Я ходжу до школи.
```

<details><summary>English translation</summary>

```text
Input:  I goes to school.
Output: I go to school.
```
</details>


## Track 2: GEC+Fluency

Fluency correction is an extension of GEC that allows for broader sentence
rewrites to make a text more fluent—i.e., sounding natural to a native speaker.
Fluency corrections are more subjective and may be harder to predict.

GEC+Fluency task covers corrections for grammar, spelling, punctuation,
and fluency.

For example:
```
Input:  Існуючі ціни дуже високі.
Output: Теперішні ціни дуже високі.
```

<details><summary>English translation</summary>

```text
Input:  Existing prices are very high.
Output: Current prices are very high.
```
</details>

## Data

### Training data

We suggest using UA-GEC for training. You can find the original dataset and
its description [here](https://github.com/grammarly/ua-gec).

We provide a preprocessed version of UA-GEC for your convenience. The two main
dirs for the two tracks are:
- [data/gec-only](./data/gec-only)
- [data/gec-fluency](./data/gec-fluency)

Each of these folders contains a similar set of files:

- `train.src.txt` and `valid.src.txt` -- original (uncorrected) texts
- `train.src.tok` and `valid.src.tok` -- original (uncorrected) texts, tokenized with Stanza.
- `train.tgt.txt` and `train.tgt.tok` -- corrected text, untokenized and tokenized versions
- `train.m2` and `valid.m2` -- train and validation data annotated in the M2 format.

The M2 format is the same as used in [CoNLL-2013](https://www.comp.nus.edu.sg/~nlp/conll13st.html)
and [BEA-2019](https://www.cl.cam.ac.uk/research/nl/bea2019st/) shared tasks.
You don't have to work with it directly, although you can.

### Use of external data

We encourage you to use any external data of your choice.

You can also prepare your own pre-processed version of UA-GEC if you want to.

In addition, feel free to submit corrections to the provided data via a pull
request if you happen to find an error.

### Validation and test data

The validation data provided with the shared task can be used for model
selection.

The final model will be evaluated on a hidden test set. See [Submission](#submission) for
details.

We annotated the test set with multiple annotators in order to somewhat
compensate for the subjectivity of the task. If a correction is in agreement
with at least one annotator, it will be counted as a valid one.


## Evaluation

### Evaluation script

We provide a script that you can use for evaluation on the validation data.

1. Install the requirements:

```bash
pip install -r requirements.txt
```

2. Run your model on `./data/{gec-fluency,gec-only}/valid.src.txt` (or `.tok.txt`
   if you expect tokenized data). Your model should produce a corrected output.
   Let's say, you saved your output to a file called `valid.tgt.txt`

3. Run the evaluation script on your output file:

```bash
scripts/evaluate.py valid.tgt.txt --m2 ./data/gec-only/valid.m2
```

If your output is already tokenized, add the `--no-tokenize` switch to the
command above.

Under the hood, the script tokenizes your output with Stanza (unless
`--no-tokenize` provided) and calls [Errant](https://github.com/chrisjbryant/errant)
to do all the heavy lifting.

### Evaluation metrics

The script should give you an output like this:

```
=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
107     18166   2044    0.0059  0.0497  0.0071
=========== Span-Based Detection =============
TP      FP      FN      Prec    Rec     F0.5
873     17393   1813    0.0478  0.325   0.0576
==============================================
```

Correction F0.5 is the primary metric used to compare models. In order to get a
true positive (TP), your edit must match at least one of the annotators' edits
exactly -- both span and the suggested text.

To get a TP in span-based detection, it is enough to correctly identify
erroneous tokens. The actual correction doesn't matter here.


## Submission

System submissions and the leaderboard are managed through the Codalab
environment: https://codalab.lisn.upsaclay.fr/competitions/10740

The test sets for both tracks can be accessed via Codalab. Requirements for
the submission files, as well as sample submission files, have been added for
your convenience.

The participants of the shared task agree to compete in a fair and honest
manner, make their solutions publicly available, and not share the test data
with any third parties.


## Results

The shared task was closed on March 10, 2023. See the leaderboards and the
winners below.

The winner for Track 1 (GEC only) is **QC-NLP** scoring 0.7314 F0.5!
Congratulations to you, Frank Palma Gomez, Alla Rozovskaya, and Dan Roth! 🎉

![Track 1. Leaderboard](img/ua-gec-track-1-leaderboard.png)

The winner for Track 2 (GEC+Fluency) is **Pravopysnyk** scoring 0.6817 F0.5!
Congratulations to you, Maksym Bondarenko, Artem Yushko, Andre Shportko, and
Andriy Fedorych! 🎉

![Track 2. Leaderboard](img/ua-gec-track-2-leaderboard.png)

The full shared task report with detailed system descriptions will be presented
and published at [UNLP](https://unlp.org.ua/) on May 5, 2023.


## Publication

Participants in the shared task are invited to submit a paper to the UNLP 2023
workshop. Please see the [UNLP website](https://unlp.org.ua/) for details.
Accepted papers will appear in the ACL anthology and will be presented at a
session of UNLP 2023 specially dedicated to the Shared Task.

Submitting a paper is **not mandatory** for participating in the Shared Task.


## Important Dates

December 20, 2023 — Shared task announcement  
February 12, 2023 — Registration deadline  
February 13, 2023 — Release of test data to registered participants  
February 20, 2023 — Shared Task paper submission  
March 10, 2023 — Submission of system responses  
March 14, 2023 — Results of the Shared Task announced to participants  
March 17, 2023 — Notification of acceptance  
March 27, 2023 — Camera-ready Shared Task papers due  
May 5, 2023 — Workshop dates


## Contacts

Telegram group: https://t.me/unlp_2023_shared_task

Email: oleksiy.syvokon@gmail.com


## References

* [UNLP 2023 Call for Papers](https://unlp.org.ua/call-for-papers/)
* Syvokon, O., & Nahorna, O. (2021). UA-GEC: Grammatical Error Correction and Fluency Corpus for the Ukrainian Language. arXiv. https://doi.org/10.48550/arXiv.2103.16997
