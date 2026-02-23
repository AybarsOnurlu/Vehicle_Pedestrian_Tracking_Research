"""
FormatConverter - Annotation format unification.

Converts annotations from heterogeneous public datasets into
the unified YOLO format: `class_id center_x center_y width height`
(all values normalized 0.0-1.0 relative to image dimensions).

Coordinate transformation (MOT → YOLO):
    cx = (x_min + w/2) / img_width
    cy = (y_min + h/2) / img_height
    nw = w / img_width
    nh = h / img_height

Public API:
    class FormatConverter:
        def convert_mot_to_yolo(mot_path, output_dir, img_size, class_mapping) -> None
        def convert_kitti_to_yolo(kitti_path, output_dir, class_mapping) -> None
        def convert_coco_to_yolo(coco_json, output_dir, class_mapping) -> None
        def convert_waymo_to_yolo(tfrecord_path, output_dir, class_mapping) -> None
"""
