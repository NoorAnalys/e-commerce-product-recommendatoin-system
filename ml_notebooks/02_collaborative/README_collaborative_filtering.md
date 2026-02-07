# Collaborative Filtering - Complete Workflow

## 📁 Project Structure

```
02_collaborative/
├── 01_cf_model_training.ipynb    ← START HERE: Train the model
├── 02_cf_evaluation.ipynb        ← THEN RUN: Evaluate the model
└── README.md                      ← This file
```

---

## 🎯 What This Does

Builds a **collaborative filtering recommendation system** using:
- **Algorithm**: Alternating Least Squares (ALS) from `implicit` library
- **Data Format**: COO sparse matrices for efficiency
- **Approach**: User-item interaction matrix (no feature engineering needed)

---

## 🔄 Complete Workflow

### Step 1: Train the Model
**Notebook**: `01_cf_model_training.ipynb`

**What it does:**
1. Loads your preprocessed Amazon data
2. Encodes user/item IDs to numerical codes
3. **SPLITS data into train (80%) and test (20%)**
4. Creates TWO interaction matrices (train and test)
5. Trains ALS model on TRAIN data only
6. Saves model, matrices, and mappings

**Output files:**
```
ml_service/app/models/collaborative_filtering/
├── als_model.pkl          # Trained model
├── train_matrix.npz       # Training interactions
├── test_matrix.npz        # Test interactions (for evaluation)
├── user_mapping.csv       # User code → User ID
├── item_mapping.csv       # Item code → Product ID
└── metadata.pkl           # Model parameters
```

---

### Step 2: Evaluate the Model
**Notebook**: `02_cf_evaluation.ipynb`

**What it does:**
1. Loads trained model and data
2. **Evaluates on TEST data** (model never saw this!)
3. Calculates metrics:
   - Precision@K: Relevance of recommendations
   - Recall@K: Coverage of relevant items
   - Catalog Coverage: Diversity of recommendations
4. Creates visualizations
5. Shows example recommendations

**Output files:**
```
/ml_service/app/models/collaborative_filtering/
├── evaluation_results.csv      # Metrics table
├── evaluation_summary.txt      # Detailed report
└── evaluation_metrics.png      # Visualization
```

---

## 🔑 Key Concepts Explained

### Why Train-Test Split?

**❌ WITHOUT SPLIT (Wrong):**
```
All Data (100%)
      ↓
Train on 100%
      ↓
Test on same 100%
      ↓
Fake good results!
```

**✅ WITH SPLIT (Correct):**
```
All Data (100%)
      ↓
Split: 80% train + 20% test
      ↓
Train on 80%
      ↓
Test on 20% (unseen)
      ↓
REAL performance!
```

**Analogy:**
- Without split = Giving students the exact exam questions beforehand
- With split = Testing students on NEW questions to see if they learned

---

### Why Use COO Matrix?

**Problem**: Most users haven't interacted with most items
```
Regular Matrix (Users × Items):
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]  ← Mostly zeros!
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
... 99% zeros, wastes memory
```

**Solution**: COO (Coordinate) Matrix
```
Only store non-zero values:
(user_0, item_4, value=1)
(user_1, item_2, value=1)
(user_2, item_6, value=1)
... saves 99% of memory!
```

---


**Why?** 
- Collaborative filtering learns from WHO interacted with WHAT
- It discovers patterns like: "Users who liked A also liked B"
- Features are for content-based or hybrid systems

---

## 📊 Understanding Evaluation Metrics

### Precision@K
**Question**: Of the K items we recommended, how many were relevant?

**Formula**: `Hits in top K / K`

**Example**:
```
Recommended 10 items → User liked 2 of them
Precision@10 = 2/10 = 0.20 (20%)
```

**Interpretation**:
- 10% = Poor (only 1 in 10 recommendations is good)
- 20% = Okay (typical for implicit feedback)
- 50%+ = Excellent (rare for CF systems)

---

### Recall@K
**Question**: Of all items the user likes, how many did we recommend in top K?

**Formula**: `Hits in top K / Total relevant items`

**Example**:
```
User likes 20 items total
We recommended 10 items → 4 were among the 20
Recall@10 = 4/20 = 0.20 (20%)
```

**Interpretation**:
- Shows if we're missing user's interests
- Higher K → Higher recall
- Trade-off with precision

---

### Coverage
**Question**: What % of items CAN the model recommend?

**Formula**: `Unique recommended items / Total items * 100`

**Example**:
```
Catalog has 10,000 items
Model recommends 4,500 unique items across all users
Coverage = 4,500/10,000 = 45%
```

**Interpretation**:
- <20% = Recommending only popular items (bad)
- 30-50% = Good diversity
- >70% = May be recommending irrelevant items

---

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas numpy scipy implicit scikit-learn matplotlib seaborn tqdm
```

### Execution
```python
# 1. Train the model
# Open and run: 01_cf_model_training.ipynb
# This takes 5-15 minutes depending on data size

# 2. Evaluate the model
# Open and run: 02_cf_evaluation.ipynb
# This takes 10-30 minutes depending on sample size
```

---

## 📝 Checklist

Before running, make sure you have:
- [x] Preprocessed Amazon data with `user_id` and `product_id` columns
- [x] Data saved in accessible location
- [x] Required libraries installed
- [x] Enough memory (sparse matrices are efficient, but still need RAM)

After running:
- [x] Check that models folder was created
- [x] Verify train/test split sizes make sense
- [x] Review evaluation metrics
- [x] Examine example recommendations

---

## ⚠️ Common Issues

### Issue: "Memory Error"
**Solution**: 
- Reduce data size
- Increase system RAM
- Use CSR format instead of COO for operations

### Issue: "Evaluation too slow"
**Solution**: 
- Reduce `SAMPLE_USERS` parameter in evaluation notebook
- Start with 500-1000 users for faster results

### Issue: "Low precision scores"
**Solution**: 
- This is NORMAL for collaborative filtering!
- Real-world CF systems typically get 10-25% precision
- Focus on improving recall and coverage instead

### Issue: "Can't find files"
**Solution**: 
- Check file paths match your directory structure
- Ensure training notebook completed successfully
- Verify all files were saved in models folder

---

## 🎓 Key Takeaways

### What You Learned:
1. ✅ **Train-test split is ESSENTIAL** for any ML model
2. ✅ **Collaborative filtering doesn't need features** - just interactions
3. ✅ **Sparse matrices save memory** for large-scale systems
4. ✅ **Separate training and evaluation** is a best practice
5. ✅ **Real metrics > Fake metrics** - always test on unseen data

### What Makes This Approach Correct:
- Split data BEFORE training
- Train on 80%, test on 20%
- Model never sees test data
- Metrics reflect REAL performance
- Can trust results for production

### What Was Wrong Before:
- Training on 100% of data
- No separate test set
- Couldn't evaluate properly
- Results were misleading
- Would fail in production
