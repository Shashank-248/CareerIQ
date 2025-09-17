# CareerIQ Frontend Bootstrap (Planned)

Initial RN/Expo scaffold to implement soon:

## Planned Screens (Phase 1)
- OnboardingScreen (UUID generation, language select)
- ProfileSetupScreen (degree, semester, interests)
- ChatScreen (connects to /api/v1/chat/ask)
- SkillsScreen (view/update skills)
- OpportunitiesScreen (fetch list)
- DailyChallengeScreen (fetch /challenges/daily)

## API Base
```
const API_BASE = 'http://192.168.1.100:8000/api/v1'; // update via discovery
```

## Device Registration Flow
1. Collect device stats via react-native-device-info
2. POST /device/register -> store tier + model plan
3. Use tier in chat request payloads

## Next Steps
- Initialize Expo project
- Implement simple global store (Redux Toolkit)
- Add service wrapper with fetch + error handling
- Add optimistic skill upsert UI
