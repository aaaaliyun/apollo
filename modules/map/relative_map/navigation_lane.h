/******************************************************************************
 * Copyright 2018 The Apollo Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *****************************************************************************/

/**
 * @file
 * @brief This file provides the declaration of the class `NavigationLane`.
 */

#pragma once

#include <list>
#include <memory>
#include <tuple>
#include <unordered_map>
#include <utility>

#include "modules/common/vehicle_state/proto/vehicle_state.pb.h"
#include "modules/localization/proto/localization.pb.h"
#include "modules/map/relative_map/proto/navigation.pb.h"
#include "modules/map/relative_map/proto/relative_map_config.pb.h"
#include "modules/perception/proto/perception_obstacle.pb.h"

/**
 * @namespace apollo::relative_map
 * @brief apollo::relative_map
 */
namespace apollo {
namespace relative_map {

// A navigation path tuple.
//
// first element: original navigation line index of the current navigation path.
// A negative value indicates illegal.
//
// second element: half of the lateral distance to the left adjacent navigation
// path, that is, the left width of the lane generated by this navigation path.
// If the navigation path is generated based on lane markers, the value is the
// perceived left lane width. If there is no left adjacent navigation path, the
// value is "default_left_width_". A negative value indicates illegal.
//
// third element: half of the lateral distance to the right adjacent navigation
// path, that is, the right width of the lane generated by this navigation path.
// If the navigation path is generated based on lane markers, the value is the
// perceived right lane width. If there is no right adjacent navigation path,
// the value is "default_right_width_". A negative value indicates illegal.
//
// fourth element : a shared pointer of the current navigation path.
typedef std::tuple<int, double, double, std::shared_ptr<NavigationPath>> NaviPathTuple;

// A stitching index pair.
// pair.first: the start stitching index of the current navigation line.
// pair.second: the end stitching index of the current navigation line.
typedef std::pair<int, int> StitchIndexPair;

// A projection index pair.
// pair.first: projection index of the vehicle in the current navigation line.
// pair.second: the distance between the vehicle's initial position and the
// projection position in the current navigation line.
typedef std::pair<int, double> ProjIndexPair;

/**
 * @class NavigationLane
 * @brief NavigationLane generates a real-time relative map based on navagation
 * lines.
 *
 * First, several navigation lines are received from the `NavigationInfo`
 * object;
 *
 * Second, several navigation line segments with the length of about 250 m are
 * cut from the whole navigation lines and the UTM coordinates are converted
 * into local coordinates with the current position of the vehicle as the
 * origin;
 *
 * Third, the navigation line segment of the vehicle's current lane is merged
 * with the perceived lane centerline.
 *
 * Fourth, a real-time relative map is dynamically created based on navigation
 * line segments and perceived lane width;
 *
 * Fifth, the relative map is output as a `MapMsg` object pointer.
 */
class NavigationLane 
{
public:
        NavigationLane() = default;
        explicit NavigationLane(const NavigationLaneConfig& config);
        ~NavigationLane() = default;

        /**
        * @brief Set the configuration information required by the `NavigationLane`.
        * @param config Configuration object.
        * @return None.
        */
        void SetConfig(const NavigationLaneConfig& config);

        /**
        * @brief Update navigation line information.
        * @param navigation_info Navigation line information to be updated.
        * @return None.
        */
        void UpdateNavigationInfo(const NavigationInfo& navigation_info);

        /**
        * @brief Set the default width of a lane.
        * @param left_width Left half width of a lane.
        * @param right_width Right half width of a lane.
        * @return None.
        */
        void SetDefaultWidth(const double left_width, const double right_width) 
        {
                default_left_width_ = left_width;
                default_right_width_ = right_width;
        }

        /**
        * @brief Generate a suitable path (i.e. a navigation line segment).
        * @param
        * @return True if a suitable path is created; false otherwise.
        */
        bool GeneratePath();

        /**
        * @brief Update perceived lane line information.
        * @param perception_obstacles Perceived lane line information to be updated.
        * @return None.
        */
        void UpdatePerception(const perception::PerceptionObstacles& perception_obstacles) 
        {
                perception_obstacles_ = perception_obstacles;
        }

        /**
        * @brief Get the generated lane segment where the vehicle is currently
        * located.
        * @param
        * @return The generated lane segment where the vehicle is currently located.
        */
        NavigationPath Path() const 
        {
                const auto& current_navi_path = std::get<3>(current_navi_path_tuple_);
                if (current_navi_path) 
                {
                        return *current_navi_path;
                }
                return NavigationPath();
        }

        /**
        * @brief Generate a real-time relative map of approximately 250 m in length
        * based on several navigation line segments and map generation configuration
        * information.
        * @param map_config Map generation configuration information.
        * @param map_msg A pointer which outputs the real-time relative map.
        * @return True if the real-time relative map is created; false otherwise.
        */
        bool CreateMap(const MapGenerationParam& map_config, MapMsg* const map_msg) const;

private:
        /**
        * @brief Calculate the value of a cubic polynomial according to the given
        * coefficients and an independent variable.
        * @param c0 Cubic polynomial coefficient.
        * @param c1 Cubic polynomial coefficient.
        * @param c2 Cubic polynomial coefficient.
        * @param c3 Cubic polynomial coefficient.
        * @param x Independent variable.
        * @return Calculated value of the cubic polynomial.
        */
        double EvaluateCubicPolynomial(const double c0, const double c1, const double c2, const double c3, const double x) const;

        /**
        * @brief Calculate the curvature value based on the cubic polynomial's
        * coefficients and an independent variable.
        * @param c1 Cubic polynomial coefficient.
        * @param c2 Cubic polynomial coefficient.
        * @param c3 Cubic polynomial coefficient.
        * @param x Independent variable.
        * @return Calculated curvature value.
        */
        double GetKappa(const double c1, const double c2, const double c3, const double x);

        /**
        * @brief In a navigation line segment, starting from the point given by
        * `start_index`, the matched point after the distance `s` is calculated, and
        * the index of the matched point is given.
        * @param path The specific navigation line segment.
        * @param start_index The index of the starting point.
        * @param s The distance from the starting point.
        * @param matched_index The pointer storing the index of the matched point.
        * @return The matched point after the distance `s`.
        */
        common::PathPoint GetPathPointByS(const common::Path& path, const int start_index, const double s, int* const matched_index);

        /**
        * @brief Generate a lane centerline from the perceived lane markings and
        * convert it to a navigation line segment.
        * @param lane_marker The perceived lane markings.
        * @param path The converted navigation line segment.
        * @return None.
        */
        void ConvertLaneMarkerToPath(const perception::LaneMarkers& lane_marker, common::Path* const path);

        /**
        * @brief A navigation line segment with the length of about 250 m are cut
        * from the whole navigation lines and the UTM coordinates are converted
        * into local coordinates with the current position of the vehicle as the
        * origin.
        * @param line_index The index of the navigation line segment vector.
        * @param path The converted navigation line segment.
        * @return True if a suitable path is created; false otherwise.
        */
        bool ConvertNavigationLineToPath(const int line_index, common::Path* const path);

        /**
        * @brief Merge the navigation line segment of the vehicle's current lane and
        * the perceived lane centerline.
        * @param line_index The index of the navigation line segment vector.
        * @param path The merged navigation line segment.
        * @return None.
        */
        void MergeNavigationLineAndLaneMarker(const int line_index, common::Path* const path);

        /**
        * @brief Update the index of the vehicle's current location in an entire
        * navigation line.
        * @param path The entire navigation line. Note that the path here refers to
        * the entire navigation line stored in UTM coordinates.
        * @param line_index The index of the whole navigation line vector stored in a
        * `NavigationInfo` object.
        * @return Updated projection index pair.
        */
        ProjIndexPair UpdateProjectionIndex(const common::Path& path, const int line_index);

        /**
        * @brief If an entire navigation line is a cyclic/circular
        * route, the closest matching point at the starting and end positions is
        * recorded so that the vehicle can drive cyclically.
        * @param
        * @return None.
        */
        void UpdateStitchIndexInfo();

private:
        // the configuration information required by the `NavigationLane`
        NavigationLaneConfig config_;

        // received from topic: /apollo/perception_obstacles
        perception::PerceptionObstacles perception_obstacles_;

        // received from topic: /apollo/navigation
        NavigationInfo navigation_info_;

        // navigation_path_list_ is a list of navigation paths. The internal paths
        // are arranged from left to right based on the vehicle's driving direction.
        // A navigation path is the combined results from perception and navigation.
        std::list<NaviPathTuple> navigation_path_list_;

        // the navigation path which the vehicle is currently on.
        NaviPathTuple current_navi_path_tuple_;

        // when invalid, left_width_ < 0
        double perceived_left_width_ = -1.0;

        // when invalid, right_width_ < 0
        double perceived_right_width_ = -1.0;

        // The standard lane width of China's expressway is 3.75 meters.
        double default_left_width_ = 1.875;
        double default_right_width_ = 1.875;

        // key: line index,
        // value: last projection index pair in the "key" line.
        std::unordered_map<int, ProjIndexPair> last_project_index_map_;

        // key: line index,
        // value: stitching index pair in the "key" line.
        std::unordered_map<int, StitchIndexPair> stitch_index_map_;

        // in world coordination: ENU
        localization::Pose original_pose_;
};

}  // namespace relative_map
}  // namespace apollo
