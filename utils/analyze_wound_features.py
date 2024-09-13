def analyze_wound_features(feature_scores, lang='th'):
    # Define thresholds and translations
    thresholds = {
        'th': {
            'ต่ำ': 20,
            'กลาง': 25,
            'สูง': 30
        },
        'en': {
            'low': 20,
            'medium': 25,
            'high': 30
        }
    }
    
    translations = {
        'th': {
            'Dominant Wound Color': 'สีบาดแผลที่โดดเด่น',
            'Presence of Pus': 'การมีหนอง',
            'Presence of Scab': 'การมีเปลือกแห้ง',
            'Wound Swelling': 'การบวมของบาดแผล',
            'Wound Temperature': 'อุณหภูมิของบาดแผล',
            'Wound Odor': 'กลิ่นของบาดแผล',
            'Wound Moisture': 'ความชื้นของบาดแผล',
            'Wound Texture': 'เนื้อสัมผัสของบาดแผล',
            'Pain Level': 'ระดับความเจ็บปวด',
            'Wound Depth': 'ความลึกของบาดแผล',
            'Wound Edges': 'ขอบของบาดแผล',
            'Skin Color': 'สีผิวรอบข้าง',
            'Skin Integrity': 'ความสมบูรณ์ของผิวรอบข้าง',
            'Red': 'แดง', 'Purple': 'ม่วง', 'Yellow': 'เหลือง', 'White': 'ขาว', 'Black': 'ดำ',
            'low': 'ต่ำ', 'medium': 'กลาง', 'high': 'สูง'
        }
    }

    def classify_score(score):
        lang_thresholds = thresholds.get(lang, thresholds['en'])
        for level, threshold in sorted(lang_thresholds.items(), key=lambda x: x[1], reverse=True):
            if score >= threshold:
                return level
        return min(lang_thresholds, key=lang_thresholds.get)

    def translate(key):
        return translations.get(lang, {}).get(key, key)

    # Analyze wound color
    wound_color_features = [key for key in feature_scores if 'Wound Color' in key]
    wound_color = max(wound_color_features, key=lambda x: feature_scores[x]).split(': ')[1] if wound_color_features else 'None'

    # Analyze other features
    analysis = {
        translate('Dominant Wound Color'): translate(wound_color),
    }

    feature_mapping = {
        'Presence of Pus': 'Presence of Pus',
        'Presence of Scab': 'Presence of Scab',
        'Wound Swelling': 'Wound Swelling',
        'Wound Temperature': ['Wound Temperature: Warm', 'Wound Temperature: Normal'],
        'Wound Odor': ['Wound Odor: Unpleasant', 'Wound Odor: Neutral'],
        'Wound Moisture': ['Wound Moisture: Dry', 'Wound Moisture: Moist'],
        'Wound Texture': ['Wound Texture: Smooth', 'Wound Texture: Rough'],
        'Pain Level': ['Pain Level: High', 'Pain Level: Low'],
        'Wound Depth': ['Wound Depth: Superficial', 'Wound Depth: Partial Thickness', 'Wound Depth: Full Thickness'],
        'Wound Edges': ['Wound Edges: Regular', 'Wound Edges: Irregular', 'Wound Edges: Undermined'],
        'Skin Color': ['Skin Color: Normal', 'Skin Color: Hyperpigmented', 'Skin Color: Hypopigmented'],
        'Skin Integrity': ['Skin Integrity: Intact', 'Skin Integrity: Fragile', 'Skin Integrity: Inflamed']
    }

    for key, value in feature_mapping.items():
        if isinstance(value, str):
            score = feature_scores.get(value, 0)
        else:
            score = sum(feature_scores.get(v, 0) for v in value)
        analysis[translate(key)] = translate(classify_score(score))

    return analysis