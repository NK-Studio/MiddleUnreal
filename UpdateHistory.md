## 1.0.2.7 : 2022-10-20 17:41:17

### Bugfix
##### Editor
  - [Entity] SK Mesh가 Costume Set 형식의 Modular라면 AnimSet Detail 창의 Facial Skeleton이 잘 못 지정되는 문제 수정 (#t4f-396)
  - [LevelEditor] T4Framework Mode에서 EventZone 타입의 NPC 스폰 시 발생하는 크래시 수정 (#t4f-406)
  - [Common] 에디터 종료 시 InventoryBase::Finalize에서 간헐적으로 발생하는 크래시 수정 (#t4f-406),

## 1.0.2.6 : 2022-10-20 16:03:06

### New feature or Enhancement
##### Editor
  - [Action] 플레이어 스폰 시 이동 및 점프 관련 값을 Testing 옵션을 통해 제어할 수 있는 옵션 추가 (#t4f-397)
    - 기본값(0)을 사용할 경우 Character Entity의 경우 Entity Testing 값을 사용
  - [Action] FacialAnimation Action, LiveLink 레코딩 시 자동 녹화 딜레이 및 종료 옵션 추가 (#t4f-374)
  - [Level] T4Framework Mode내 MainProject SpawnData 와 Replay를 플레이할 수 있는 기능 추가 (#t4f-403)

### Bugfix
##### Editor
  - [Entity] Costume Entity, CostumePartMeshData에서 bFace처리 삭제 - PartName이 Face만 체크 (#t4f-396)
  - [Common] T4F 에디터에서 오픈한 레벨을 레벨에디터에서 다시 오픈할 경우 발생하는 크래시 수정 (#t4f-395)

## 1.0.2.5 : 2022-10-18 17:00:45

### New feature or Enhancement
##### Editor
  - [Action] Animation/ControlRig/FacialAnimation Track 우클릭 서브메뉴에 Change PlayMode Duration (AutoFit) 추가 (#t4f-374)
  - [Action] Facial Animation Action내 LiveLinkFace와 연동한 AnimSequence 레코딩 기능 추가 (#t4f-374)
  - [Entity/Portrait Generator] 애니메이션의 일부 구간을 지정한 Sec 간격으로 다수의 이미지를 생성해주는 기능 추가 (#t4f-360)

### Bugfix
##### Editor
  - [Action] Reaction Action이 타임라인 TogglePlay(Pause/Play)가 적용되지 않던 문제 수정 (#t4f-380)
  - [Entity] Skill Layer의 AnimSequence Name (Skill)이 추가되지 않는 문제 수정 (#t4f-378)
  - [Animation] 메타휴먼 데이터가 없는 사용자 프로젝트 쿠킹 시, 메타휴먼용 Facial Anim Instance Cook 오류 문제 수정 (#t4f-391)
\t- 에디터 실행 시 meta human data 존재 여부에 따라  target skeleton을 변경
  - [Animation] Facial AnimBP의 live link 관련 노드가 깨지는 문제 수정 (#t4f-391),

## 1.0.2.4 : 2022-10-14 18:35:43

## 1.0.2.3 : 2022-10-14 17:44:07

### New feature or Enhancement
##### Editor
  - [Entity] Portrait 설정 시 Facial Anim Layer에 있는 Animation Section 도 사용할 수 있도록 옵션 기능 처리 (#t4f-377)
  - [Entity] Portrait 생성 이미지 품질 개선 (모아레 제거, 최대 4096 해상도까지 지원) (#t4f-382)
  - [Entity] Entity/Portrait Preview World로 MapEntity를 사용할 수 있도록 기능 처리 (#t4f-361)

### Bugfix
##### Client or Server 
  - [Server] NPC Behavior 옵션 EnemyType 설정이 정상적으로 동작하지 않던 문제 수정 (#t4f-369)

##### Editor
  - [Action] 시뮬레이션 모드에서의 좌클릭 액션 플레이가 동작하지 않던 문제 수정 (#t4f-379)
    - 좌클릭은 리플레이 등의 다른 기능과 연계가 많아 편집 중인 액션 플레이를 \"F\" 키로 변경함
  - [Action] Timeline TogglePlay 시 Animation/Facial Track의 애니메이션이 반응하지 않던 문제 수정 (#t4f-380)

### AssetUpdate (Dev to TD)
  - Content\\VirtualFlow\\SystemPack\\System\\AnimBP\\RefSkeleton\\BP_Human_MetaHuman_Face_Skeleton
  - Content\\VirtualFlow\\SystemPack\\System\\AnimBP\\RefSkeleton\\RefMocap\\mh_arkit_mapping_anim
  - Content\\VirtualFlow\\SystemPack\\System\\AnimBP\\RefSkeleton\\RefMocap\\mh_arkit_mapping_pose
  - Content\\VirtualFlow\\SystemPack\\System\\AnimBP\\T4AnimBP_Human_BasicFace
  - Content\\VirtualFlow\\SystemPack\\System\\AnimBP\\T4AnimBP_Human_MetaHumanFace

## 1.0.2.2 : 2022-10-13 19:13:37

### Bugfix
##### Editor
  - [World] 실행 시 간헐적으로 설정된 MapEntity 레벨 로드 시 발생하는 크래시 예외 처리 (#t4f-376)

##### Common
  - [Common] 패키징 종료 시 발생하는 크래시 수정 (#t4f-375)

## 1.0.2.1 : 2022-10-13 14:01:01

### New feature or Enhancement
##### Client or Server
  - [Editor/Client] TileBase일때 장비창의 Costume의 Group분류 (#t4f-339)
  - [Client] 점프 중 충돌 시, 점프는 종료하고 낙하 상태로 전이되도록 수정 (#t4f-365)

##### Editor
  - [Action] CameraWork Action 프로퍼티 이름 변경 (Use Looping => Pause At The End) (#t4f-321)
    - 마지막 카메라 위치에서 멈추는 옵션이라 네이밍을 정리함

##### Common
  - [Action] Facial Animation Action 기능 추가 (#t4f-299)
    - 참조 : [Facial Animation Action 제작](https://virtualflow.atlassian.net/wiki/spaces/VIRTUALFLOWINTERNAL/pages/98631702/Face+Mesh+Module+Facial+Animation+Action)


### Bugfix
##### Client or Server 
  - [Client/Server] NPC 간 이동중 충돌이 발생할 경우 클라이언트 위치가 어긋나는 문제 수정 (#t4f-367)
  - [Editor/Client] 특정한 상황에서 Dialogue 2D의 Z order가 꼬이는 문제 (#t4f-333)
  - [Editor/Client] PIE Mode, NPC와의 인터렉트 이후 Quest를 통해 영상 재생 시 이전 대화 상자가 Hide 되지 않는 문제 (#t4f-353)
  - [Client] DialogueTalk의 UseLookAt 옵션 적용이 일정 시간 이후 초기화 되는 문제 수정 (#t4f-321)
  - [Server] Effect의 Chain Effect로 Hit Effect를 사용하는 경우, 데미지 적용이 되지 않는 문제 수정 (#t4f-337)

##### Editor
  - [GameDB] 일부 구버전 프로젝트DB 테이블의 폴더 내 아이템이 DB에 출력되지 않던 문제 수정 (#1230)
  - [Character/Costume] Customizing Rig가 적용 된 부분(Face)이 MaterPart가 될 때, Mesh 출력이 되지 않는 문제 수정 (#t4f-355)

### AssetUpdate (Dev to TD)
  - #t4f-339 테이블 데이터 업데이트
   - Localization/Editor/T4EditorMasterConstantTable.uasset
   - Localization/Editor/Constants/T4Constant_EquipPartsGroupTable.uasset
   - Localization/System/T4GameplayEquipPartsGroupDataTable.uasset,

## 1.0.2.0 : 2022-10-09 21:37:23

### New feature or Enhancement
##### Editor
  - [Common] 에디터 StatusBar \"버추얼플로우 스튜디오\" 레이아웃 개선 (#t4f-359)

### Bugfix
##### Client or Server 
  - [Common] 2단점프와 Enable Movement While Jumping 옵션이 동작하지 않는 문제 수정 (#t4f-348)

##### Editor
  - [World] Map Entity 오픈 후 WorldExplorer에서 Map Entity 세팅 시 발생하는 크래시 수정 (#t4f-356)
    - 해당 조건에서는 메시지를 띄운 후 WorldExplorer 실행을 취소하도록 처리 (다른 툴을 닫고 다시 시도)
  - [World] 미니맵 생성을 위해 Map Entity 세팅 시 발생하는 크래시 수정 (#t4f-349)
  - [Action] Timeline Play or Pause로 편집 ActionPack 플레이가 정상적으로 동작하지 않던 문제 수정 (#t4f-305)
  - [Entity] Weapon Entity, EditMode AttachPoint 변경 시 기즈모 업데이트가 되지 않던 문제 수정 (#t4f-357)
,

## 1.0.1.11 : 2022-10-06 15:30:07

### Bugfix
##### Editor
  - [Entity] MapEntity Detail, 활성화된 탭과 상관없이 모든 설정 메뉴가 노출되는 문제 수정 (#t4f-352)

##### Common
  - [Common] Duration이 설정된 Skill의 ActionPack이 출력되지 않던 문제 수정 (#t4f-350)

## 1.0.1.10 : 2022-10-06 10:31:54

### Bugfix
##### Editor
  - [Content] 특정 프로젝트(TutorialGame_Example)의 DB설정이 정상적으로 적용되지 않던 문제 수정 (#t4f-350)
  - [Entity] Map Entity, Level Asset 초기 설정 후 뷰포트 월드 로드 시 발생하는 ensure 및 종료 시 에러 수정 (UE5) (#t4f-349)

## 1.0.1.9 : 2022-10-05 16:06:46

### [New feature or Enhancement]
##### Editor
  - [Action] 좌측 레이아웃에 EntityBrowser 추가 (#t4f-305)
  - [Entity] EntityBrowser에서 Costume 좌클릭 SubMenu로 교환 시도 시 플레이어 Skeleton과 같을 경우만 교환 가능하도록 개선 (#t4f-305)
  - [Entity] JumpLoop 모션을 PlayRate를 맞추어 한번만 재생하는 System Parameter 옵션 추가 (#t4f-344)
  - [Entity] 통합 점프 사용 여부에 따른 점프 관련 Parameter Data 숨김 처리 추가 (#t4f-345)
##### Common
  - [Editor Common] Bookmark가 비어있을 경우 \"현재 위치로 북마크 업데이트\" 버튼으로 북마크가 추가되도록 개선 (#t4f-305)

### [Bugfix]
##### Client or Server 
  - [Client] 파라미터로 분리한 JumpLand 뒷부분이 복구 모션으로 출력되지 않는 문제 수정 (#t4f-346)
##### Editor
  - [Content] Costume, Weapon Type의 Item은 Stackable이 동작하지 않고 있던 문제 수정 (#t4f-318)
  - [GameDB] 비어있는 DB Category Tab 선택 시 이전 탭에서 편집중이던 DB Item 정보가 Details에 표시되던 문제 수정 (#t4f-314)
  - [Action] 기본 Map Entity 변경 시 로컬에 실제 레벨 에셋이 없을 경우 발생하는 크래시 수정 (#t4f-320)
  - [World] 편집 대상인 Map Entity 이 로컬에 존재하지 않을 경우 발생하는 크래시 수정 (t4f-340)
##### Common
  - [Common] 리플레이로 스폰된 액터가 플레이어 이동에 충돌되는 문제 수정 (#t4f-343)
    - World RayCasting 관련 코드가 변경되어 기존 캐릭터 피킹, 점프, 낙하, 캐릭터간 충돌 등의 기본 기능 점검 필요
,

## 0.0.0.0 : 2022-10-04 18:44:54,

## 0.0.0.0 : 2022-10-04 18:22:38,

# 1.0.1.8 : 2022-09-30 16:19:15

### [New feature or Enhancement]
##### Client or Server
  - [Client] Guest 모드시 캐릭터 생성 못하는 문제 수정 (#t4f-327)
##### Editor
  - [Action] 초기 PreviewEntity 스폰 시 Bookmark에 설정된 동일 맵의 저장 위치로 캐릭터가 스폰되도록 개선 (#t4f-320)

### [Bugfix]
  - [Entity] Weapon/Costume Entity 생성 후 오픈 시 발생하는 크래시 수정 (#t4f-247)

# 1.0.1.7 : 2022-09-29 17:50:45

### [New feature or Enhancement]
##### Client or Server
  - 인벤토리 UITemplate 타입 추가 for MetaHuman (#t4f-314)
##### Editor
  - [Action] ControlRig Action 편집 시 캐릭터 Mesh에 Default Animation Rig 데이터가 설정되어 있다면 활용할 수 있도록 기능 추가 (#t4f-246)
  - [Customizing Rig] Rig 정보의 Min/Max Property를 Start/End로 변경하고 Start/End의 값 크기를 비교하여 증감할 수 있는 로직으로 수정 (#t4f-329)
  - [Customizing Rig] Rig 작업 내용을 비슷한 SK구조를 가진 Face에 적용할 수 있도록 Export/Import하는 기능 제공 (#t4f-330)

### [Bugfix]
##### Common
  - [Common] NPC Waypoint 이동 및 리플레이 플레이에서 캐릭터 이동 중 캐릭터 간 충돌 방지 옵션이 동작하지 않던 문제 수정 (#t4f-334)

### AssetUpdate (Dev to TD)
- #t4f-314 [리소스 업데이트]
  - Content\VirtualFlow\UIPack\Common\T4Builtin_Common_Message.uasset
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinDBBrowserWidget.uasset
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinEquipmentWidget_1.uasset
  - Content\VirtualFlow\UIPack\T4BuiltinLoginMainWidget_1.uasset
  - Content\VirtualFlow\UIPack\Template\TileBase\Common\T4InventoryTab_TileBase.uasset (New)
  - Content\VirtualFlow\UIPack\Template\TileBase\InGame\T4Inventory_TileBase.uasset (New)
  - Content\VirtualFlow\UIPack\Template\TileBase\InGame\T4InventoryLayout_TileBase.uasset (New)
  - Content\VirtualFlow\UIPack\Template\TileBase\Item\T4InventoryListItem_TileBase.uasset (New)

# 1.0.1.6 : 2022-09-27 17:54:25

### [New feature or Enhancement]
##### Client or Server
##### Editor
  - [Action] Replay Action Details에서 ReplaySystemAsset의 일부 데이터를 편집할 수 있도록 기능 오픈 (#t4f-320)  
  - [Entity] AnimSet에 등록된 시퀀스 일부/전체를 대상으로, FootStep 노티파이를 자동 생성하는 기능 추가 (#t4f-278)  
  - [Content] 프로젝트 저장 시 마스터테이블도 함께 저장되도록 개선 (#t4f-326)
  - [Content] ProjectDB Add/Duplicate/Remove 후 Undo시 발생하는 크래시 수정 (#t4f-316)
##### Common

### [Bugfix]
##### Client or Server 
  - [Client] 프로젝트 설정에서 GuestMode 선택 시 플레이어 TextDB가 비었을 경우 로그인 실패 문제 수정 (#t4f-328)
##### Editor
  - [Entity] Character Entity 생성 시 크래시가 발생하는 문제 수정 (#t4f-325)
  - [Content] VirtualFlow Studio 메뉴를 열면 현재 생성되어 있는 모든 프로젝트의 StagingData의 테이블 값이 갱신 되는 문제 수정 (#t4f-323)
##### Common

### AssetUpdate (Dev to TD)
- [리소스 수정] UIPack\InGame\T4BuiltinHUDShortcutWidget.uasset

# 1.0.1.5 : 2022-09-26 10:21:11

### [New feature or Enhancement]
##### Editor
  - [Content] ProjectDB의 값이 변경됐을 때 관련 원본 데이터가 실시간 갱신 되도록 개선 (#t4f-296)
  - [Action] ActionPackBorwser 필터에 사용하는 ParentEntity의 Skeleton이 동일할 경우에도 함께 표시되도록 개선 (#t4f-305)
  - [Action] Replay Action 추가 (Experimental) (#t4f-305)
    - 클라이언트, 에디터에서 녹화한 리플레이를 ActionTrack으로 추가해 플레이 할 수 있도록 지원
	- N개의 리플레이를 동시에 플레이 할 수 있도록 지원
	- 플레이중인 N개의 리플레이를 합쳐서 녹화 할 수 있도록 지원
  - [Entity] Costume Entity의 메타휴먼 BP에서 파츠 가져오기 기능에 특정 파츠만 선택해 가져올 수 있는 기능 추가 (#t4f-307)
 
### [Bugfix]
##### Client or Server 
  - [Client] 공용메세지 위젯에 메세지가 반영되지 않는 문제 (#t4f-308)
  - [Client] ItemDescription의 Button Text가 정상적으로 노출되지 않는 문제 (#t4f-311)
 
##### Editor
  - [Content] T4F(v1.0.1.4)가 한번도 안 깔려 있던 컴퓨터에서 최초설치 후 첫 실행에서 Project DB를 읽지 못하는 문제 수정 (#t4f-268)
  - [Action] Timeline의 Duration Section 마우스 선택이 정상적으로 동작하지 않던 문제 수정 (#t4f-205)
  - [Action] Track 메뉴의 To Front/End 버튼 사용 시 플레이 중인 액션이 정지되지 않던 문제 수정 (#t4f-305)

# 1.0.1.4 : 2022-09-21

### [New feature or Enhancement]
##### Client or Server
  - [Editor/Client] Editor UI Template 지원 기능 (#t4f-303)
##### Common
  - [Common] 캐릭터 얼굴 커스터마이징이 가능한 Character Spawn 기능 개발 (#t4f-247)
    - [캐릭터 커스터마이징 Asset 제작 및 사용법](https://virtualflow.atlassian.net/wiki/spaces/VIRTUALFLOWINTERNAL/pages/78184450/Asset)

### [Bugfix]
##### Editor
  - [Entity] MetaHuman Character Spawn 후 땅으로 꺼지는 문제 수정 (#t4f-293)
  - [Common] 새 저장소에서 에디터 실행 시 발생하는 크래시 수정 (#t4f-315)
  - [Common] 에디터 리플레이 녹화를 위해 툴바의 SaveDialog 오픈 시 기본 디렉토리가 정상적으로 보이지 않던 문제 수정 (#t4f-305)
  - [Common] Costume Entity로 CostumeSet 사용 시 AttachParts가 출력되지 않던 문제 수정 (#t4f-307)


# 1.0.1.3 : 2022-09-20
### [New feature or Enhancement]
##### Editor
  - [Common] VirtualFlowStudio StatusBar 페이지 내 공지사항용 WebBrowser 임베딩 (#t4f-290)
    - https://t4framework.com/Notice.html/Notice_KR.html 연결
  - [Common] VirtualFlowStudio의 MainProject 설정이 Confing/DefaultT4Framework.ini 에 저장되도록 개선 (#t4f-290)
    - T4FrameworkEditorSettings Section
  - [Common] T4Framework 용어 관제 작업 (한/영) 3차 진행 (#t4f-304)

### [Bugfix]
##### Client or Server 
  - [Client] InventorySlotMax일때 마우스 픽업 경고메세지 출력 추가 (#t4f-291)
##### Editor
  - [UserInterface] 기존의 T4UserInterface에셋을 콘텐츠브라우저에서 열 때 엔진 크래쉬가 나는 문제 (#t4f-302)
  - [Content] ProjectSettings 설정 Clear 시 발생하는 크래시 수정 (#t4f-297)
  - [Entity] Costume Entity의 AttachParts 설정이 ParentEntity를 변경해도 반영되지 않던 문제 수정 (#t4f-300)
  - [Entity] Goods Entity의 DropMesh 설정 메뉴가 출력되지 않던 문제 수정 (#t4f-306)
  - [Common] Weapon/Costume Entity의 DropMesh 설정이 있을 경우 테스팅 옵션과 관계없이 프리뷰에 드랍메시가 출력되던 문제 수정 (#t4f-301)


# 1.0.1.2 : 2022-09-15
### [New feature or Enhancement]
##### Client or Server
  - [Client] 점프 착지 중 궤적 대로 이동하지 않고, 목표 위치로 캐릭터 위치가 Set 되는 문제 수정 (#t4f-292)
  - [Client] 제자리 점프 시 착지 모션이 재생되지 않는 문제 수정 (#t4f-294)
  - [Client] Inventory에 수용 가능한 숫자가 10개로 제한되는 이슈 (#t4f-291)
##### Editor
  - [Common] 에디터 Status Bar 에 VirtualFlow Studio 탭(구 T4Projects) 추가 (#t4f-290)

### [Bugfix]
##### Editor
  - [Content] T4Framework 최초 실행 시, 기존프로젝트의 DB를 찾을 수 없는 문제 수정 (#t4f-268)

### AssetUpdate (Dev to TD)
- #t4f-291 DEV/TD 모두 업데이트
  - Content\VirtualFlow\Localization\System\T4GameplayMessageDataTable.uasset
  - Content\VirtualFlow\UIPack\Common\T4Builtin_Common_Message.uasset
  - Content\VirtualFlow\UIPack\Common\T4Builtin_DescriptionItem.uasset
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinInventoryWidget.uasset

# 1.0.1.1 : 2022-09-14
### [New feature or Enhancement]
##### Editor
  - [Common] 에디터 초기 가동 시 레벨에디터 탭에 VirtualFlowStudio 탭(구 T4Projects)가 활성화 되도록 개선 (#t4f-290)
### [Bugfix]
##### Client or Server 
  - [Client] 두 System Layer 애니메이션 BlendTime 동안 Idle이 나오는 문제 수정 (#t4f-283)
##### Editor
  - [Content] StatLevelDB Editor - Detail 패널의 편집 내용이 저장되지 않던 문제, StatDB Editor - Description 편집 내용이 TreeView에 바로 반영되지 않던 문제 수정 (#t4f-284)
  - [Entity] Entity Editor, Costume/Weapon Detail - Default - Item Spawn Type에 출력되던 EquipOrExchange => EquipOrModularMesh로 용어 수정 (#t4f-287)
##### Common
  - [Common] 에디터 환경에서 메타휴먼 사용 시 Groom(HairStrands) 디버깅 정보가 표시되던 문제 수정 (#t4f-274)
  - [Common] MetaHuman 캐릭터 스폰 시 SkeletalMesh 가 지하로 꺼지는 문제 수정 (#t4f-293)

# 1.0.1.0 : 2022-09-07
### [New feature or Enhancement]
##### Client or Server
  - [Client] C/S 동기화를 위한 OffsetTime 을 감안한 애니메이션 재생 처리 추가 (#t4f-271)
##### Editor
  - [LevelEditor] LevelEditor T4Framework Mode의 플레이어 스폰 기능 추가 (#t4f-128)
  - [Editor] Skill Animation DropList ##### EditorConstantDB Add 기능 추가 (#t4f-264)
  - [Content] 프로젝트 DB 테이블 버전 관리 개선 (#t4f-273)
### [Bugfix]
##### Client or Server 
  - [Editor/Client] Dialogue2D Custom Anim 편집을 위해 UMG 연결 (#t4f-270)
  - [Client] UE5에서 폰트 컬러등 표시 안됨 우회 코드 정리 (#t4f-277)
  - [Editor] 새로 생성한 Project의 UserConstantTable데이터 추가가 안되는 문제 (#t4f-275)
  - [Client] 점프 중 이동키 입력에 의해 캐릭터가 궤적에서 벗어나는 문제 수정 (#t4f-279) 
##### Editor
  - [Entity] Costume/Weapon Entity Detials 및 탭 메뉴 정리 (#t4f-287)
  - [Entity] MetaHuman, MasterParts의 LODSync 설정이 적용되지 않던 문제 수정 (#t4f-285)
  - [Entity] MetaHuman, Torso만 등록된 CostumeEntity 변경 시 MasterParts Body가 소실되는 문제 수정 (#t4f-282)
  - [Entity] MetaHuman, AttachParts Hair만 설정된 CostumeEntity에 대한 파츠 교환이 안되던 문제 수정 (#t4f-282)
  - [Entity] 첫 Entity 오픈 시 카메라 방향 및 거리 오류 수정 (#t4f-155)
  - [Persona] IK Rig나 IK Retargeter 에디터 실행 시 크래시 나는 문제 수정 (#t4f-280)
  - [Physics Asset] Physics Asset 에디터에서 정상적으로 Physics Asset이 설정되지 않는 문제 수정 (#t4f-281)
### AssetUpdate (Dev to TD)
- <주의>
  - Localization 수정은 TD에도 미리 올려주세요.
  - Dev/TD 동시 업데이트가 불가한 에셋은 Content 폴더 이하 경로를 모두 적어주세요.
- #t4f-277 (수동 업데이트 예정)
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinSayWidget.uasset
  - Content\VirtualFlow\UIPack\T4Builtin_CreatCharacter_Widget.uasset
  - Content\VirtualFlow\UIPack\T4BuiltinLobbyMainWidget.uasset
  - Content\VirtualFlow\UIPack\T4BuiltinLoginMainWidget.uasset

# 1.0.0.0 : 2022.08.29
### HOTFIX-2 (2022.08.31)
- Bugfix
  - [Client] Dialogue2D Animation이 UE5에서 실행되지 않는 현상 (#t4f-269)
  - [Content] Spawn Object 뷰포트 복수 선택에 Shift + 클릭 뿐 아니라 Ctrl + 클릭도 되도록 지원 (#t4f-230)
  - [Editor] 데이터가 존재하지 않는 User Constant Table은 Main Project가 되어도 상수테이블이 갱신되지 않던 문제 수정 (#t4f-259)

### HOTFIX-1 (2022.08.31)
- Bugfix
  - [Client] 점프 준비 중 점프가 취소된 이후, 점프 시도 시 JumpReady 애니메이션이 출력되지 않는 문제 수정 (#t4f-262)
  - [Client] 단차가 있는 곳에서 JumpReady - JumpStart 사이 FallLand 출력되는 문제 수정 (#t4f-263)

### [New feature or Enhancement]
##### Client or Server
  - [Client] CreateWidget 만들어 쓰는 Widget들 일부 WidgetManager로 등록 (#t4f-218)
  - [Client] Widget의 연출 기능 추가 (#t4f-235)
  - [Client] UT4BuiltinButton 기능 확장과 Widget 버튼 교체 (#t4f-240)
  - [Client] 점프 시간이 착지 모션 길이보다 작을 때, Start/Loop 없이 Land 뒷부분을 우선적으로 재생하도록 수정 (#t4f-253) 
  - [Client/Server] JumpReadyTimeSec 이후 공중에 뜨도록 패킷 전송 시점 수정 (#t4f-257)
  - [Editor/Client] Dialogue 화자의 2DTexture 지원 (#t4f-244)
  - [Client] JumpLand 뒷부분을 복구 모션으로 사용하는 경우, 재생 시작 시점에 이동 시, Run 모션이 나오지 않는 문제 수정 (#t4f-261)
##### Editor
  - [Content] Project Category = Storytelling 사용 시 GameDB 출력 프로퍼티 제어 (#t4f-242)
    - 아이템 장착, 스킬 관련 프로퍼티 일부 오픈 (Player/NPC/Weapon/Skill)
    - ActionPack 설정에서 불필요한 프로퍼티 제외 (Weapon/Skill)
  - [Content] Camera Type의 Spawn Object는 Camera Anchor가 출력되도록 처리 (#t4f-222)
  - [Content, Action] Spawn Camera Default Mesh, Waypoint Path Segments, ActionPack Camera Anchor의 Selected, Unselect Mesh 변경 (#t4f-221)
    - DefaultT4FrameworkEditor.ini, DefaultT4FrameworkCore에 사용 Mesh 노출화
  - [Action] CameraWork Track Section 선택 또는 Scrubbing 시 카메라 위치 표시 및 PreviewActor 출력 동기화 (#t4f-241)
  - [Action] CameraWork Action 내 Bezier Curve 동작 추가 (DisableBezierCurve로 미사용 옵션 선택 가능) (#t4f-241)
  - [Entity] Entity Editor, Preview Scene - T4PreviewLevel 추가 (#t4f-220)
  - [Entity] Entity Editor - Preview Viewport 기본 레벨을 T4PreviewLevel로 변경 (#t4f-225)
  - [Editor] T4Framework 용어 관제 2차 작업 반영 (#t4f-238)
  - [Entity] 여러 동작이 포함된 시퀀스 하나를 단독 사용하는 경우를 위한 Integrated Jump 옵션 추가 (#t4f-227) 
    - 참조 : https://virtualflow.atlassian.net/wiki/spaces/VIRTUALFLOWINTERNAL/pages/41680938/Jump+Control+Animation
  - [Editor] T4ProjectBrowser에 MainProject를 선택할 수 있는 기능 추가 (#t4f-251)
  - [Entity, Action] 상단 툴바에 Main Project를 선택할 수 있는 기능 추가 (#t4f-250)
  - [Editor] Expand toolbar 목록에 보여지는 메뉴 명이 T4EditorMessageDataTable을 따라가도록 개선 (#t4f-255)
  - [Content, Entity] PlayerDB - Locomotion Data 와 Entity Details - Testings 에 JumpReadyTimeSec 프로퍼티 추가 (#t4f-257)
##### Common
  - [Server] 세션 패킷 분리 로직 ParallelFor로 수정 (#T4F-233)

### [Bugfix]
##### Client or Server 
  - [Server] 퀘스트 미디어 멀티 플레이 컨트롤 규칙에 따라 동작 안되는 오류 수정(#T4F-35)
  - [Client] 제자리 회전을 사용하지 않는 경우, 점프시 수직으로 점프되는 문제 수정 (#t4f-231)
##### Editor
  - [EditorCommon] PreviewActor(CameraWork/Waypoint)의 FOV 및 AspectRatio 값이 InGame 정보와 틀린 문제 수정 (#t4f-241)
  - [Content] Spawn Object 복수 선택시 기즈모 편집이 한 개의 Object 밖에 적용이 안 되는 문제 수정 (#t4f-230)
  - [Content] Project 파일 삭제 후 동일 이름으로 재생성시 기존 Project 파일의 Layer 이름이 재생성된 Project Viewport에서 보이는 문제 수정 (#t4f-200) 
  - [Content] QuestFlow, Project Asset 등록시 그래프가 자동 갱신되지 않던 문제 수정 (#t4f-243) 
  - [Action] CameraWork Start/End 구간 SourceCamera LookAtPoint 사용이 정상적으로 동작하지 않던 문제 수정 (#t4f-241)
  - [Action] ActionPack 오픈 시 사용자가 편집한 Action Track의 순서로 정렬되지 않던 문제 수정 (#t4f-248)
  - [Action] CameraWork Track에서 SectionKey 추가 시 DebugLine 출력 오류 수정 (#t4f-236)
  - [Action] ControlRig/CameraWork Track 셀렉션 변경 시 간헐적으로 CameraWork Anchor가 삭제되는 문제 수정 (#t4f-101)
  - [Action] ControlRig Action 의 SaveAnimSet 기능이 동작하지 않던 문제 수정 (#t4f-101)
  - [Entity] 대소문자 구분이 안되는 문제로 AnimSetTemplate => AnimTemplate으로 Enum, Prooperty명 변경 (#t4f-237)
  - [Content] QuestFlow, TimeWait노드 노드액션이 작동되지 않는 문제 수정 (#t4f-252) 
  - [Content] QuestFlow, Empty Composite에 '데코레이터 영역 적용' 옵션이 출력되던 문제 수정 (#t4f-254) 

### AssetUpdate (Dev to TD)
- #t4f-240 (TD업데이트 이후 수동 업데이트 예정)
  - Content\VirtualFlow\UIPack\Common\T4Builtin_DescriptionItem.uasset
  - Content\VirtualFlow\UIPack\Common\T4Builtin_Stat.uasset
  - Content\VirtualFlow\UIPack\Common\T4BuiltinButton.uasset
  - Content\VirtualFlow\UIPack\Common\T4BuiltinButtonExt.uasset (New)
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinEquipmentLayoutWidget.uasset
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinInventoryLayoutWidget.uasset
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinOptionWidget.uasset
  - Content\VirtualFlow\UIPack\T4Builtin_CreatCharacter_Widget.uasset
  - Content\VirtualFlow\UIPack\T4BuiltinLobbyMainWidget.uasset
  - Content\VirtualFlow\UIPack\T4BuiltinLoginMainWidget.uasset
- #t4f-244  (TD업데이트 이후 수동 업데이트 예정)
  - Content\VirtualFlow\UIPack\Common\T4Builtin_MediaWidget.uasset
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinDialogueWayWidget.uasset
  - Content\VirtualFlow\UIPack\InGame\T4BuiltinDialogueWidget.uasset
